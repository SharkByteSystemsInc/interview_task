Run docker-compose.yml and check how program performs. Fix problems from TODO list. 

TODO LIST:

- Make sure proper message bytes conversion
- Eliminate redundant message sending with same data
- Propose proper connection wait on other service
- Add feature (modify flow):
    - service ping starts with message with value 0 as INITIALIZER
    - service pong receive data add 1 to int value and send it back to ping 
    - service ping receive data add 1 to int value and send it back to pong
    - services close when max reached


Is ZMQ good for communication between services?