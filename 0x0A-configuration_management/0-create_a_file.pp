file { '/tmp/school':
  ensure  => 'file',     # Ensures it's a regular file
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
