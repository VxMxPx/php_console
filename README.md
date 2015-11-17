# PHP Console

**See: https://github.com/VxMxPx/Evalify for newer version written in Vala.**

A tiny Python3 application using GTK3, which allow you to simply
execute a PHP script without saving it. It's useful when you want to quickly
test a multi-line code snippet. It's in a way fancy version of `php -a`.

![](php-console.png)

Right now only one command is available (`F5`) which will execute the code.

The code will be saved to `/tmp` and when you open the application next time,
it will load your previous code. But since this is `/tmp` code will not survive
reboots, so don't rely on it.

## Changelog

- 2014-10-05:
    - Added scrollbars
    - Added support for realtime checkcing

## Future plans

... if I won't be too lazy or too busy:

- change location to which code is being saved,
- turn it to proper application (organize rename files, make icon, etc..),
- make it available on AUR,
- allow code to be executed as you type,
- remember position and size,
- better shortcuts (CTRL+Q to exit, CTRL+Enter to execute code)
- offer some options, like:
    - font family, font size,
    - color scheme for syntax highlighting,
    - tab width,
    - location where code is being saved,
    - PHP location and parameters
- allow multiple tabs

## License

The PHP Console application is licensed under the GPL-3.0 or later.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
