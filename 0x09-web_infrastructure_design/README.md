# 0x09. Web Infrastructure Design

This project is part of the Full Stack Software Engineering curriculum at ALX. It focuses on understanding the principles of designing a web infrastructure.

## Key Concepts
- :globe_with_meridians: Network basics
- :desktop_computer: Server
- :computer: Web server
- :gear: Application server
- :globe_with_meridians: DNS & DNS record types
- :balance_scale: Load Balancer
- :chart_with_upwards_trend: Monitoring
- :file_cabinet: Database
- :warning: Single point of failure
- :globe_with_meridians: HTTP & HTTPS
- :shield: Firewall

## File Descriptions

The project consists of multiple files, each of which represents a stage in designing a web infrastructure:

### [0-simple_web_stack](0-simple_web_stack)

In this stage, you design a basic web infrastructure on a whiteboard. The infrastructure hosts a website accessible via `www.foobar.com`. It starts with a user wanting to access your website. You must include the following components:

- :desktop_computer: 1 physical server
- :computer: 1 web server (Nginx)
- :gear: 1 application server
- :file_cabinet: 1 application files (your code base)
- :file_cabinet: 1 database (MySQL)
- :globe_with_meridians: 1 domain name `foobar.com` configured with a `www` record that points to your server's IP address `8.8.8.8`.

### [1-distributed_web_infrastructure](1-distributed_web_infrastructure)

In this stage, you expand the web infrastructure to include three servers that host the website `www.foobar.com`. You build upon the components in [0-simple_web_stack] and add:

- :desktop_computer: 2 physical servers
- :computer: 1 web server (Nginx)
- :gear: 1 application server
- :balance_scale: 1 load-balancer (HAproxy)
- :file_cabinet: 1 set of application files (your code base)
- :file_cabinet: 1 database (MySQL)

### [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)

In this stage, you enhance the web infrastructure to make it secure, enable encrypted traffic, and implement monitoring. Building on [1-distributed_web_infrastructure], you include:

- :shield::shield::shield: 3 firewalls
- :lock: 1 SSL certificate to serve `www.foobar.com` over HTTPS
- :chart_with_upwards_trend: 3 monitoring clients (data collectors for Sumologic or other monitoring services)

### [3-scale_up](3-scale_up)

This final stage further expands the infrastructure designed in [2-secured_and_monitored_web_infrastructure]. You incorporate:

- :desktop_computer: 1 physical server
- :balance_scale: 1 load-balancer (HAproxy) configured as a cluster with the existing one
- :file_cabinet: Split components (web server, application server, database) with their own servers.

## File Overview

| Filename                                     | Description                                              |
| -------------------------------------------- | -------------------------------------------------------- |
| [0-simple_web_stack](./0-simple_web_stack)   | Design a basic LAMP stack web infrastructure.            |
| [1-distributed_web_infrastructure](./1-distributed_web_infrastructure) | Expand the infrastructure with additional components. |
| [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure) | Enhance security and monitoring. |
| [3-scale_up](./3-scale_up)                   | Further scale up the infrastructure.                    |


