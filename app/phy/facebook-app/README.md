
---
layout: page
title:  "How to generate Facebook app access tokens as developer"
categories: [ app ]
---

1. create profile
2. verify account as per [help center](https://www.facebook.com/help/167551763306531) with mobile number or credit card
3. add developer to app
4. as developer, accept this
5. register as developer https://developers.facebook.com/async/registration/
6. generate on https://developers.facebook.com/tools/explorer for the app a Page Access Token and select the page on the popup. To be able to post onto the page include the permissions
  - pages_read_engagement
  - pages_manage_posts
7. paste on https://developers.facebook.com/tools/debug/accesstoken/ and extend this token
8. paste that token on https://developers.facebook.com/tools/explorer/ for the path /me/acounts and receive in the middle field a long-lived access token

