# Sets up your client SSH configuration file to add a private key
include stdlib

file_line { 'Allow use of private key':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'IdentityFile ~/.ssh/holberton',
}

file_line { 'Shut off Passwd Auth':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
}
