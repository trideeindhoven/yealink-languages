# yealink-languages

The goal of this repository is to create a comprehensive library of international language resources for Yealink phones.
There are a few reasons for starting this repository:
1. Maybe you need a language that is not supported
2. Maybe your local language is embargoed (yes! e.g. the Dutch language is embargoed by the company Lydis)
3. Maybe your language is supported, but you would like to improve the translation.

We keep track of the progress of the translations. Because we use automated software for the translations new translations can (and will) be made available quickly. Here you can find the progress of the translationfiles:  
<img src="https://progress-bar.dev/87?title=Dutch%20T41S&width=120" />  
<img src="https://progress-bar.dev/87?title=Dutch%20T46S&width=120" />  
<img src="https://progress-bar.dev/91?title=Dutch%20T46G&width=120" />  
<img src="https://progress-bar.dev/87?title=Dutch%20T48S&width=120" />  
<img src="https://progress-bar.dev/89?title=Dutch%20CP860&width=120" />  

This repository contains languagefiles ordened per phonetype. If you want to provision your phone with a new language, use the following two entries in your provisioning document:

```
gui_lang.url = Dutch
gui_lang.url = https://raw.githubusercontent.com/trideeindhoven/yealink-languages/main/T46S/017.GUI.Dutch.lang
```

It is an ambition to create a "language-provision-and-redirect" service somewhere in Q3 2021. That means you just redirect your phone to:
https://provisioning.domain.com/Dutch?redirect=https://provisioning.yourcompany.com/yealink

Then the firmware gets updated, language gets installed and your phone gets redirected to your own provisioning server (or Yealink RPS if you prefer). This is a one-time provisioning path you need to do after which the redirection service will no longer be involved with your phone!

Obviously we will be maintaining a LOT of translations for A LOT of phones, so pull requests are welcome! A good guide on how to create pull requests can be found at:
https://opensource.com/article/19/7/create-pull-request-github

Please don't forget to create a new branch. That is important.

In every "phonetype" directory we have placed the English translationfile. That is a good way to start translating. It is not necessary to translate the full file in one go. This is what github is great at: version control! Just do whatever work you want to do and create the pull request.  
Thank you very much!
