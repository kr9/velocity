---
title: 'The ultimate 2-hour networking setup that protects your privacy'
description: 'A step-by-step guide to a privacy-first home network using Asus RT-AC68U, NordVPN, Asuswrt-Merlin firmware, and DNS encryption in under 2 hours.'
publishedAt: 2017-12-04
author: 'Kamal Rupareliya'
image: ../../assets/images/wp/RemoteHouse1-1.jpg
imageAlt: 'Remote house with privacy networking setup'
tags: ['networking', 'privacy', 'router', 'vpn', 'wifi']
draft: false
featured: false
category: 'Technology'
---

The ISPs are doing everything in their power to compel us to do a lot of work to protect our privacy. Fortunately, if we put some effort, we can protect our privacy and also make a dent in their attempt.

![](../../assets/images/wp/RemoteHouse1-1-1024x683.jpg)

Well, it is not practical to move to a beautiful, but remote, island just to protect our privacy. The ISPs are doing everything in their power to compel us to do so. Fortunately, if we put some effort, we can protect our privacy and also make a dent in their attempt. As a privacy believer, I keep exploring options. I am noticing that more and more people are getting aware of privacy and options are now better than they were a couple of years back.

This weekend I spent some time bumping up the privacy of my complete setup as my old [Asus RTN66U](https://www.amazon.com/gp/product/B006QB1RPY/) was not keeping up with the current requirements. I was already using Nord VPN to access my IP restricted servers from anywhere. I added some flair to it. First I created the summary for my future reference and then thought about publishing it for the benefit of other people who are actively trying to protect their privacy. I will be brief. I have provided a few links if you like to dig deeper.

## 1. [Asus RT-AC68U](https://www.amazon.com/gp/product/B00FB45SI4/) — the new router

I first tried [NETGEAR R7900-100NAS Nighthawk X6 AC3000](https://www.amazon.com/gp/product/B0106N5OOW/) after going through its shiny specs for the value and some good reviews. The deal-breaker was the lack of intuitive VPN support or the ability to install [DD-WRT](https://dd-wrt.com/). You will see reviews about Netgear everywhere, but I am not sure why that company is not investing anything in upgrading its web interface. For me, it feels like Netgear doesn't give a damn about customers' productivity. I ended up getting a new [Asus RT-AC68U](https://www.amazon.com/gp/product/B00FB45SI4/). I realized that AC1900 is plenty for current needs and will probably be good for the next few years. It seems very stable and mature.

## 2. [Asuswrt-Merlin](https://www.asuswrt-merlin.net/) — custom firmware

I decided to use it with Asuswrt-Merlin firmware to get some more customization. It might not be as good as DD-WRT interface but this [article](https://dfarq.homeip.net/asuswrt-merlin-vs-dd-wrt/) helped me to go with Merlin.

## 3. [Nord VPN](https://nordvpn.com/) — the VPN service

I think it is reasonably priced with versatile apps and options. It makes your connection a little slow, as does the rest of the VPNs due to added processing. I would recommend turning the router-level VPN off if you want to use serious bandwidth on multiple devices. During that time, you can always enable VPN on your computer or smartphone VPN app. It will also be handy when certain websites try to block the VPN IP.

## 4. [AB-Solution](https://www.ab-solution.info/) — the router level ad-blocker

I have yet to validate the practicality of it, but it has been a few hours and I am liking it. To save some time, please go through installation [requirements](https://www.ab-solution.info/install/requirements.html) first. I chose Option 2 (Medium) during the [installation](https://www.ab-solution.info/install/install.html) stage 3. It is the only confusing part and I guess it will work well for most. You will have to access your router using SSH. You can enable SSH on Asus by referring to this [link](https://www.htpcguides.com/enable-ssh-asus-routers-without-ssh-keys/). To connect, use `ssh [admin username]@[router IP]`, usually `admin@192.168.1.1` in Terminal. You will also need a permanently plugged-in USB on the router, formatted with ext2 file system. Mac doesn't allow you to format in ext2 natively. You may use a trial of [Paragon](https://backstage.paragon-software.com/home/extfs-mac/).

## 5. [DNS.watch](https://dns.watch/index) — the secure DNS service

It is really necessary to use a neutral, fast, no-logging and uncensored DNS service to protect your privacy and freedom. I chose DNS.Watch by trusting in what they believe.

## 6. [DNS Crypt](https://dnscrypt.org/) — secure queries to DNS server

DNSCrypt authenticates communication between your computer and a DNS resolver (DNS.watch). It prevents DNS spoofing. It verifies that responses are coming from the intended DNS server and haven't been modified. It is free and vendor agnostic. Download DNS Crypt for Mac using this direct [link](https://github.com/alterstep/dnscrypt-osxclient).

It is not as time-consuming as it seems. Here is a summary to help you save more time:

1. Get a VPN service — [Nord VPN](https://nordvpn.com/)
2. Get a VPN-friendly router — [Asus RT-AC68U](https://www.amazon.com/gp/product/B00FB45SI4/)
3. Install [Asuswrt-Merlin](https://asuswrt.lostrealm.ca/) on router and configure Nord VPN [with Merlin](https://nordvpn.com/tutorials/asustwrt-merlin/openvpn/) or [without](https://nordvpn.com/tutorials/asuswrt/openvpn/)
4. Install router level ad-blocker — [AB-Solution](https://www.ab-solution.info/)
5. Use custom DNS server — [DNS.watch](https://dns.watch/index)
6. Encrypt the queries to DNS server — [DNS Crypt](https://dnscrypt.org/)

I hope it will save you some time. I feel data protection is imperative for a healthy ecosystem. You can read more about it in my previous article, [Next universal civil war will be for data freedom](/blog/next-universal-civil-war-will-be-for-data-freedom/).

Photo by [Magnus Lindvall](https://unsplash.com/photos/ll3Z_SlkRIs).
