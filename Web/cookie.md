- Cookie are text files
- A cookie is created when a browser is told to create one by web server
- Instruction sent in http header
  Set-Cookie: <cookie-name>=<cookie-value>
- Browser <-------------- WebServer
             Set-Cookie
- Once a browser created a cookie, when any requests are made by the browser for the same domain,
  any cookies that belong to this domain will be sent back as part of the request

Session Cookie
--------------
- Temporary and will only be stored in the memory of the browser while it's open
- When it's closed, the cookie will be removed from browser's history
- Lower security risk because of that
- e commerce shopping carts - multi-page site visit

Persistent Cookie
-----------------
- Create persistent cookies by adding attribute "Expires" into the Set-Cookie header
- Other Attributes:
  > Secure: This tag for cookies will only be sent if the browser's request is sent through
            an encrypted protocol(https)
  > HttpOnly: When a cookie is flagged with this atrribute, it won't be accessible to JavaScript
              in the webpage's Document Object Model, and will only be transmitted back to the domain
              that issued it.
  > SameSite: Makes sure cookies are only transmitted back to their originating website.

First-Party Cookie
------------------
- Created by a site you are visiting
- Help a website carry out a number of purposes, such as allowing you to add more
  than one item to your online order

Third-Party Cookie
------------------
- Created by a site you're not currently visiting
- Third-party cookies are most commonly used to track a user who's clicked on an ad,
  associated them with the domain that's referred them.

Risks of cookies
----------------
Cookie Fraud
------------
- Cookie fraud will be a malicious website attacking another website by using
  legitimate uses as a proxy, or a legitimate user's activity being tagged with
  a false session ID.

Types of cookie fraud
---------------------
Cross-Site Scripting (XSS)
- A user will receive a cookie after they have visited a malicious website
- The cookie contains a script payload that targets another website, but the
  malicious cookie is in disguise and looks as it's come from the website
  that's being targeted.
- Therfore when a user visits the targeted site, this fraudulent cookie (and its script payload)
  is sent to the targeted site's server
- This type of vulnerability may be used by attackers to get past certain access controls
  like the same origin policy

Session Fixation
- The attacker tricks the user into using a specific session ID
- After the user logs in to the web application using the provided session ID,
  the attacker uses this valid session ID to gain access to user's account
- Session identifiers are used to authenticate users in web applicaations
- If no session identifiers, we would have to login to web applications much more frequently than we do.
- Weakness: Someone knows session ID, they get access to your account, which may be used for further attacks
            and potential privilege escalation
- How to get session identifiers?
  > Social Engineering
  > Phishing
  > Session hijacking: Getting session id from a logged-in user [MITM - Man in the middle attack]
- Session Fixation is reverse of this: The victim gets an existing session ID and is tricked into logging
  in using this identifier, which lets the attacker take over the user's sesion later.

Cross-Site Request Forgery Attack (CSRF)
- A legitimate cookie is received by a user when they visit a legitimate site
- However when they visit a malicious site which instructs the browser of the user
  to perform an action that targets the legitimate site thay have previously visited
- A request is recieved by the legitimate site alongside the legitimate cookie,
  and the same action is performed as it seems to have been triggered by the legitimate
  user, but it hasn't, it's been initiated by malicious site.

Cookie Tossing Attack
- A user is provided with a cookie by a malicious site, which has been designed to look like
  it's come from the targeted site's subdomain. (http://subdomain.placeholder.com)
- When the user goes to the targeted site (placeholder.com), all the cookies are sent, including
  legitimate ones and the subdomain cookie.
- When the cookie that's interpreted first in the subdomain, this data will overrule any of the
  legitimate data contained in the other valid cookies.

Cookie fraud, the cookies are being used to perform malicious actions using the legitimate user's
identity, or to falsify a legitimate user's identity.
