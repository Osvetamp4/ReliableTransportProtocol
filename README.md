# ReliableTransportProtocol

## High-Level Approach
Designed a reliable transport protocol on top of UDP, implementing custom packet formats with sequence numbers, checksums, and acknowledgment fields

## Challenges
Challenges that were involved in developing the SACK protocol were with the Sender logic and the buffer storage for out of order acked packets. That last part alonet ook me 15 hours at Snell to work on and fix.

A major issue we ran into was that from 3-1 and onwards, the recv was HEAVILY delayed in comparison to the Sender packets which forced me to develop the Sender a more robust code that dealt with heavily delayed ACK packets. However once we fixed that, I had to bug fix the Recv portion which was more simple as We just had to manage how the sack blocks were controlled and developed which was comparitavely not as hard and convoluted. We also faced problems with duplicate packets, where failing to properly deduplicate data led to incorrect state and unnecessary retransmissions. Another major issue was corrupted packets, which caused crashes when expected fields like "data" were missing, and required adding validation and checksum verification to safely drop malformed packets. As we progressed, delayed ACKs became a significant challenge, especially in later tests, where the sender would incorrectly assume packet loss and trigger premature retransmissions. This exposed weaknesses in our timeout logic, which initially grew too large or reacted too slowly, reducing throughput. We also had to refine our fast retransmit mechanism, ensuring that missing packets were resent based on repeated gaps rather than blindly resending large portions of the window.

## Properties/features
Reliable data transfer over UDP using sequence numbers, acknowledgments, and retransmission logic
In-order delivery guarantee through cumulative ACK tracking and buffered reassembly of out-of-order packets
Selective Acknowledgment (SACK) support to efficiently represent received packet ranges beyond the cumulative ACK
Selective retransmission of only missing packets (holes), avoiding unnecessary full-window resends
Robust handling of out-of-order packets via a receiver-side buffer and dynamic SACK block reconstruction
Duplicate packet detection and elimination to prevent redundant processing and incorrect state updates
Corruption detection using checksums, ensuring malformed packets are safely dropped without crashing the system
Adaptive congestion control (slow start + AIMD) to balance throughput and network stability
Fast retransmit mechanism triggered by repeated missing packet signals (SACK gaps) to reduce recovery latency
Dynamic RTT estimation and timeout adjustment for handling delayed ACKs and varying network conditions
Resilience to unreliable network conditions, including packet loss, duplication, jitter, and delay
Efficient bandwidth utilization by scaling the congestion window based on network feedback and ACK progress

## Tests
We tested our code using the configs file and check the error as it gives us.