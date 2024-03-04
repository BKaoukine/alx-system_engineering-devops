#Manifest that installs the Nginx package and Configure it.
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}",
  require => Package['nginx'], # Ensure Nginx package is installed before applying configuration
  notify  => Service['nginx'], # Notify Nginx service to restart when the configuration file changes
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'], # Ensure Nginx package is installed before starting the service
}

# Create index.html file with 'Hello World!' content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'], # Ensure Nginx package is installed before creating index.html
  notify  => Service['nginx'], # Notify Nginx service to restart when the index.html file changes
}
