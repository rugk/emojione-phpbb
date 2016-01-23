#Emojione for phpBB

![Preview](preview.png)

This repository provides a full installation of [Emojione](http://emojione.com/), a complete open source emoji set, to replace phpBB defaults smilies.


## Installation

1. [Download](https://github.com/sylvaindurand/emojione-phpbb/archive/master.zip) and extract the package.
2. Put `emojione` folder and `emojione.pak` file in `/images/smilies/` in your phpBB installation.
3. Put `SMILEY_LIMIT` to `3000` in `includes/constants.php`
4. In phpBB Administration Control Panel, go to `Posting` tab, then to `Smilies` section, and select `Install smilies package`.

## Extend to Emoji
Since version 3.2, phpBB automatically converts emojis to images, but from a different provider. To change it, edit `/vendor/s9e/text-formatter/src/Plugins/Emoji/Configurator.php` and change the line `return $template;` with `return '<img alt="{.}" class="smilies" src="./images/smilies/emojione/' . '{@seq}.' . 'svg" />';`.


