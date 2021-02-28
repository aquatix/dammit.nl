Title: Journaling
Started: 2020-07-17 10:01:55
Date: 2020-07-17 11:53:00
Slug: journaling
Location: Home (duh)
Authors: Michiel Scholten
Category: projects
Tags: journal, life, opensource, secondbrain
Image: https://shuttereye.org/images/64/6461b596b6373733_2000-2000.jpg
Status: published

![Tablet with stylus, notes, plants, and a cup of tea](https://shuttereye.org/images/64/6461b596b6373733_2000-2000.jpg)

It is [no secret that I keep a journal]({filename}5-minute-journal.md) (it might not be very well known too, but it is private anyway). It is not a fancy hard copy journal that some talented people fill with really neat doodles and such, but rather a boring collection of Markdown-formatted text files, put into version control (a private Git repository), because of course it is.

This journal serves as a second memory storage, to look back at what happened on a certain date, as the 5-minute-journal that keeps me grounded on the important things in life, and as a place to quickly jot down some thoughts that occurred to me.

Something I still want to do, is connect it to my [second brain]({tag}secondbrain), so I can work on the thoughts resulting from the braindump, and provide backlinks to relevant information.

As I want to keep clear daily entries, and make notes throughout the day, I quickly developed a little helper script, as a computer is good in helping with repeating tasks. My journal log files are created afresh for every new month, and have a pre-defined part and divider for every day. After that, a timestamp is entered and my favourite text editor is opened at the right place, in a distraction-free state with [Goyo](https://github.com/junegunn/goyo.vim) and [Pencil](https://github.com/reedes/vim-pencil).

I copied this little helper here wholesale, for fun and maybe to inspire someone:

    #!/bin/bash
    DATETIME=$(date +%Y%m%d\ %a\ %H:%M:%S)
    MONTH=$(date +%Y%m)
    DAY=$(date +%Y%m%d)
    DAYOFWEEK=$(date +%u)
    TIME=$(date +%H:%M)
    LOGDIR="$HOME/.my/journal/"
    LOGFILE="${LOGDIR}${MONTH}_journal.md"

    # Dutch days of the week
    DAYNL[1]='maandag'
    DAYNL[2]='dinsdag'
    DAYNL[3]='woensdag'
    DAYNL[4]='donderdag'
    DAYNL[5]='vrijdag'
    DAYNL[6]='zaterdag'
    DAYNL[7]='zondag'

    cd "${LOGDIR}" || exit

    # Convenience so scriptname can be used to do the git pushing and pulling
    if [ "${1}" == "push" ]; then
        git push
        exit
    elif [ "${1}" == "pull" ]; then
        git pull
        exit
    fi

    if [ ! -f "${LOGFILE}" ]; then
        echo "A new month has begun, starting with a fresh log"
        touch "${LOGFILE}"
        git add "${LOGFILE}"
    fi

    if ! grep -q "${DAY}" "${LOGFILE}"; then
        # No day heading for today found yet, create one
        {
            echo
            echo
            echo "## ${DAY} ${DAYNL[${DAYOFWEEK}]}"
            echo
            # Five minute journal
            #echo "I am grateful for"
            #echo "What would make today great?"
            #echo "Daily affirmations. I am"
            #echo
            #echo "3 amazing things that happened today"
            #echo "How could I have made today even better?"
            # Five minute journal, Dutch
            echo "Ik ben dankbaar voor"
            echo "Wat zou vandaag goed maken?"
            echo "Dagelijkse bevestiging. Ik ben"
            echo
            echo "Drie geweldige dingen die vandaag gebeurd zijn:"
            echo "1."
            echo "2."
            echo "3."
            echo
            echo "Hoe had ik vandaag beter kunnen maken?"
            echo ">"
            echo
            echo "Cogitorama:"
            echo
            echo "Food:"
            echo "Weer:"
        } >> "${LOGFILE}"
    fi

    echo >> "$LOGFILE"
    echo -n "${TIME} " >> "${LOGFILE}"

    if [ -z "$1" ]; then
        vim -c "setlocal spell spelllang=nl|set nofoldenable|Goyo|Pencil" '+ normal GA' "${LOGFILE}"
    else
        echo "$@" >> "${LOGFILE}"
    fi

    COMMITDATETIME=$(date +%Y%m%d\ %a\ %H:%M:%S)
    git commit "${LOGFILE}" -m "journal entry from $DATETIME saved at $COMMITDATETIME"
