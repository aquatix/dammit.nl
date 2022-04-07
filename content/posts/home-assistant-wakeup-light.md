Title: Home Assistant: wake-up light
Started: 2022-04-07 21:55:52
Date: 2022-04-07 21:55:52
Slug: home-assistant-wakeup-light
Location: Home, nerdcave
Authors: Michiel Scholten
Status: published
Category: howto
Tags: homeautomation, life, tech

Today I was hanging around in #nlhomeautomation on IRC as one does, and for some reason we started talking about alarm clocks. I wake up with a self-built wake-up light that is triggered by my Home Assistant instance and manifests as a nicely glowing bowl on my night stand that starts as dark red and slowly gains strength and transfers to a brighter white.

Add as script:

```
alias: Wake-up light slowly more bright
sequence:
  - service: light.turn_on
    data:
      rgb_color:
        - 255
        - 0
        - 0
      transition: 1
      brightness: 1
    target:
      entity_id: light.wakeup_lamp
  - delay:
      hours: 0
      minutes: 0
      seconds: 2
      milliseconds: 0
  - service: light.turn_on
    data:
      rgb_color:
        - 255
        - 0
        - 0
      transition: 1
      brightness: 3
    target:
      entity_id: light.wakeup_lamp
  - repeat:
      count: '6'
      sequence:
        - delay: '00:00:10'
        - service: light.turn_on
          data:
            transition: 3
            brightness_step: 10
          target:
            entity_id: light.wakeup_lamp
  - delay: '00:00:01'
  - service: light.turn_on
    data:
      rgb_color:
        - 255
        - 129
        - 1
      transition: 3
    target:
      entity_id: light.wakeup_lamp
  - repeat:
      count: '12'
      sequence:
        - delay: '00:00:10'
        - service: light.turn_on
          data:
            transition: 3
            brightness_step: 10
          target:
            entity_id: light.wakeup_lamp
  - service: light.turn_on
    data:
      rgb_color:
        - 255
        - 191
        - 0
      transition: 3
    target:
      entity_id: light.wakeup_lamp
  - repeat:
      count: '04'
      sequence:
        - delay: '00:00:10'
        - service: light.turn_on
          data:
            transition: 3
            brightness_step: 10
          target:
            entity_id: light.wakeup_lamp
  - service: light.turn_on
    data:
      rgb_color:
        - 255
        - 218
        - 109
      transition: 3
    target:
      entity_id: light.wakeup_lamp
  - repeat:
      count: '02'
      sequence:
        - delay: '00:00:10'
        - service: light.turn_on
          data:
            transition: 3
            brightness_step: 10
          target:
            entity_id: light.wakeup_lamp
mode: restart
icon: hass:weather-sunset
```

And then add an automation to trigger on a certain time, or whatever you want, and call a service with type "script" and the name of the above script.
