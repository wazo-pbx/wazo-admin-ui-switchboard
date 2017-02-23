install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/switchboard.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-switchboard
	rm /etc/wazo-admin-ui/conf.d/switchboard.yml
	systemctl restart wazo-admin-ui
