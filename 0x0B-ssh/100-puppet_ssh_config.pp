#Manifest to connect to server.

file { '/home/bk/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "
    Host ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
  owner   => 'bk',
  group   => 'bk',
}
