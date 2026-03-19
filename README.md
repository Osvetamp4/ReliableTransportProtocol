# ReliableTransportProtocol

SYSTEM DESIGN OVERVIEW

I developed the underlying SACK protocol whilst Harry developed the overlaying bandwidth protocol.

Challenges that were involved in developing the SACK protocol were with the Sender logic and the buffer storage for out of order acked packets. That last part alonet ook me 15 hours at Snell to work on and fix.

A major issue I ran into was that from 3-1 and onwards, the recv was HEAVILY delayed in comparison to the Sender packets which forced me to develop the Sender a more robust code that dealt with heavily delayed ACK packets. However once we fixed that, I had to bug fix the Recv portion which was thankfully a lot more simple as I just had to manage how the sack blocks were controlled and developed which was comparitavely not as hard and convoluted.