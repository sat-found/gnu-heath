<!--
SPDX-FileCopyrightText: 2024 Gerald Wiese <wiese@gnuhealth.org>
SPDX-FileCopyrightText: 2024 Leibniz University Hannover

SPDX-License-Identifier: GPL-3.0-or-later
-->

# GNU Health Dockerfile

This Dockerfile installs the GNU Health Hospital Information System (HIS).

It is based on a Python/Debian image and uses uWSGI to run the Python application.

For running it you need an accessible PostgreSQL system. Connection parameters can be set using environment variables.

This is part of a GNU Health Docker Compose setup:

https://gitlab.com/gnu-health/docker/gnu-health-docker-compose

But you could also use it separately.

Check GNU Health documentation, official source repositories and Docker repositories for further reading:

https://docs.gnuhealth.org/his

https://codeberg.org/gnuhealth/

https://gitlab.com/gnu-health/docker
