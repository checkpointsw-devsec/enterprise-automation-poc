variable "vsphere_user" {
  type = string
}

variable "vsphere_password" {
  type = string
}

variable "vsphere_server" {
  type = string
}

variable "vsphere_datacenter" {
  type = string
  default = "DC_POC_Lab"
}

variable "vsphere_datastore" {
  type = string
  default = "datastore1"
}

variable "vsphere_host" {
  type = string
  default = "172.23.23.44"
}

variable "mgmt_net" {
  description = "The virtual network for Check Point management traffic"
  default     = "Internal_1"
}

variable "remote_ovf_url" {
  type = string
  default = "http://192.168.100.53" 
}

variable "vsphere_folder_name" {
  type = string
  default = "automation-poc"
}

variable = "chkp_passwd_hash" {
  type = string
}

variable = "chkp_otp_key" {
  type = string
}

variable = "chkp_admin_password_plain" {
  type = string
} 

# This password hash is for vpn123 - please do not use this for production
chkp_passwd_hash =  "\\$6\\$UAxWXDhef2zm8mqt\\$gvnwQIF1dkw8J9JUvmyYXUeAt2LSl4V62JKNFilEK0YQGo4ACOTry4QLWjE9nMQOPCKs42ZleldciXgCdnjCd1"

# Default SIC key - please also replace this with your key
chkp_otp_key = "vpn123"

# Default admin password - plain text option. To use a hash - paste the hash value here and change the value in deploy-resilient-gateways.tf for password-type to Hash
chkp_admin_password_plain = "Cpwins12345!"
