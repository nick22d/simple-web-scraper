Vagrant.configure("2") do |config|
  # The web server hosting the coffeeshop site
  config.vm.define "web-server" do |ws|
    ws.vm.box = "ubuntu/bionic64"
    ws.vm.network "private_network", ip: "192.168.56.10"

    # Sync local coffeeshop folder to /home/vagrant/coffeeshop in the VM
    ws.vm.synced_folder "./coffeeshop", "/home/vagrant/coffeeshop"

    # Update the software repositories and install nginx
    ws.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y nginx
      sudo systemctl enable nginx
    SHELL

    # Import the necessary artifacts
    ws.vm.provision "file", source: "./coffeeshop/robots.txt", destination: "/tmp/robots.txt"
    ws.vm.provision "file", source: "nginx.conf", destination: "/tmp/nginx.conf"
    ws.vm.provision "file", source: "site.conf", destination: "/tmp/nginx-site.conf"

    # Put in place the necessary configuration
    ws.vm.provision "shell", inline: <<-SHELL
      sudo mv /tmp/robots.txt /var/www/html
      sudo mv /tmp/nginx.conf /etc/nginx/nginx.conf
      sudo mv /tmp/nginx-site.conf /etc/nginx/sites-available/default
      sudo chmod o+x /home/vagrant
      sudo chown -R www-data:www-data /home/vagrant/coffeeshop
      sudo systemctl restart nginx
    SHELL
  end
  
end
