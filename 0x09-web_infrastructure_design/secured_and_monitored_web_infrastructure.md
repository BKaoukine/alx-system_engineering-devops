# Web Infrastructure Issues

## 1. Terminating SSL at the Load Balancer

- **Issue:** When SSL (Secure Sockets Layer) is terminated at the load balancer, the internal communication between the load balancer and the servers is not encrypted.
- **Why it's a Problem:** 🔒 If accessed by malicious entities, sensitive information can be eavesdropped, posing a security risk. Keeping SSL encryption all the way to the servers ensures end-to-end security.

## 2. Having Only One MySQL Server Accepting Writes

- **Issue:** If there's only one MySQL server for write operations, it becomes a single point of failure.
- **Why it's a Problem:** ⚠️ If the MySQL server goes down, the system may be unable to write new data, leading to poor user experience and potential data loss. Redundancy and load distribution for write operations ensure reliability.

## 3. Servers with All the Same Components

- **Issue:** All servers having identical components (database, web server, application server) can lead to widespread issues.
- **Why it's a Problem:** ⚙️ If a flaw or update affects one server, it could impact all servers simultaneously. Diversity in server setup provides resilience against unexpected problems.


