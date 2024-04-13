# TASKI - simple task management

![N|Solid](https://res.cloudinary.com/dl32dhthp/image/upload/v1713038269/hznzziac27fhmgc9qt6x.png)



## Issue Summary:
![](https://res.cloudinary.com/dl32dhthp/image/upload/v1713043148/a0kp2dwowkqu1sg1mhoc.png)

The server of the web app failed and users couldn't acces their tasks, the web app was accessible but no data was shown to users.

- Duration: two hours - 9AM GMT -> 11AM GMT
- Impact: no data was shown to users
- Root cause: server

## Timeline:
![](https://res.cloudinary.com/dl32dhthp/image/upload/v1713042802/jefumpvvdqxo3raoudwj.png)
- Issue was detected at 9AM 4 FEB 2024
- Monitoring ALert on server status from DataDog
- The server was restarted
- Web framwork was checked for bugs
- The incident was escalated to the back-end team
- The incident was solved after restarting the server and fixed server rout config

## Root cause and Resolution:
![](https://res.cloudinary.com/dl32dhthp/image/upload/v1713042802/xckl7nnzi0gfdkbdpsuu.png)

> The Nginx server was configured to serve same rout twice which caused
> it to crash and failes to deliver the data requested by the user.
> The essue was solved by changing the Nginx configuration for different rout to server
> depanding on the user request and checking for any other path duplication.
> A backup server was created to ensure data delivery for best user experience upon master server future failure.

## Future Measures:
![](https://res.cloudinary.com/dl32dhthp/image/upload/v1713042802/cndxhqq2kpe7ofabj8cz.png)

To prevent this web app failure in the future the dev team will be focusing on:

| Layers | Measures |
| ------ | ------ |
| Monitoring | Setup more monitors and alerts for better insights |
| Code | Regulare maintaine of the code and updates|
| Hosting | upgrad hosting to ensure speed and performance |
| User Reports | Encourage user to report any miner essue they encounter |


> Dev TEAME: Brahim Kaoukine
