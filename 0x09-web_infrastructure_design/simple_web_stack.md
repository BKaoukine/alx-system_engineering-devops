# Simple Web Stack

This infrastructure model has three pitfalls or downsides:

1. **SPOF (Single Point of Failure):** The website depends on one server, and if this server fails, the entire system fails, preventing users from accessing the website. :x:

2. **DOWNTIME:** Since there is only one server, any modifications or deployment of new code require shutting down or restarting the server, impacting the user's experience. :alarm_clock:

3. **Overload Traffic Risk:** The server's capacity is at risk with high traffic, and there is no possibility to scale up by adding more resources or servers. :traffic_light:


