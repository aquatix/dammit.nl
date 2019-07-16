Title: Receive Sentry messages as Telegram notifications
Started: 2019-07-16 15:35:43
Date: 2019-07-16 17:51:43
Slug: sentry-to-telegram
Location: Work
Authors: Michiel Scholten
Category: howto
Tags: dev, notifications, tech, web, work
Status: published

To be able to receive [Sentry](https://sentry.io/) notifications on Telegram (without using the plugin which only works in the self-hosted Sentry server), one can use webhooks. As I have [webhaak]({filename}webhaak-all-the-things.md) to <strike>ducttape together</strike> webhook all the things, I created a script to send messages to our dev chat, filtering away some that are not relevant.

```
#!/bin/bash
set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

if [ "$#" -ne 4 ]; then
    echo "USAGE: sentry_to_telegram.sh [projectname] [culprit] [url] [message]"
    exit 1
fi

PROJECTNAME="${1}"
CULPRIT="${2}"
URL="${3}"
MESSAGE="${4}"

# Filter away known things
if [[ $MESSAGE == *"Het ElementTree object kon niet"* ||
      $MESSAGE == *"Meerdere resultaten gevonden in "* ||
      $MESSAGE == *"Found multiple results in"* ||
      $MESSAGE == *"Cannot find object for id"* ]];
then
    exit
fi

# Make the URL a bit more neat
URL=${URL//?referrer=webhooks_plugin/}

# The message to send
REPORT="[${PROJECTNAME}] ${MESSAGE}

in ${CULPRIT}

${URL}"

#REPORT="${REPORT//_/\_/}"

# AwesomeCorp dev groupchat
CHATID="-4242424242"
KEY="YOUR:KEY-HERE"
TIME="10"
URL="https://api.telegram.org/bot$KEY/sendMessage"

curl -s --max-time $TIME -d "chat_id=$CHATID&disable_web_page_preview=1&text=$REPORT" $URL >/dev/null
exit
curl -X "POST" "https://api.telegram.org/bot${KEY}/sendMessage" \
     -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
     --data-urlencode "text=${REPORT}" \
     --data-urlencode "chat_id=${CHATID}" \
     --data-urlencode "disable_web_page_preview=true" \
     --data-urlencode "parse_mode=markdown"
```

This script is called from webhaak, with a config like the following:

```
        sentry:
            triggerkey: 7c6bd635948eea920fc15df87400a45b056c9779f4305bf0
            notify: false
            command: /srv/scripts/sentry_to_telegram.sh "PROJECT_NAME" "CULPRIT" "URL" "TITLE"
```

You can see it in context in this [webhaak example config](https://github.com/aquatix/webhaak/blob/master/example_config/examples.yaml). The `notify: false` takes care no PushOver notification is sent every time the webhook is called.
