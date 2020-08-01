### Question: 

Imagine a System that will receive task via REST-API which then has to be processed on a different machine, how would you design such a system? How would you manage the load if there is only one machine that must execute all tasks? How would you manage the load if there were multiple machines to execute the tasks? Please describe.

### Reply:

![Alt text](../images/t1.png?raw=true "Scheduling servers")


### Explanation:

- The system which receives task, is to be treated as scheduling server. It can be same server or different. If there are multiple machines serving the request, they can be 
communicated via the messaging engine such as Redis (for example).
- Each machine can transmit its vital stats via a daemon embedded in each server that reports status to the redis server. And the scheduling server can then read the status of 
the servers in real time.
- Another option exist in order to create a network of computers communicating with one another. That is to have an RPC server in each machine, where we can directly 
communicate via the RPC server to instruct the servers to execute certain tasks.

- In addition to keeping tab on the scheduling servers, a FIFO queue can be created in a messaging server containing tasks to be scheudules.
- For each server (meant to execute tasks) we open up a messaging channel (meant for pub/sub communication) meant to schedule tasks for the servers.
- When a server becomes free to execute tasks, the scheduling server, then allocates from the FIFO queue, the latest task, to the messaging channel. On task completion this very channel is used to communicate the status of the job.


