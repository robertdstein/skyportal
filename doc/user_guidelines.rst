User Guidelines
===============

Skyportal is an open-source project designed to support the time-domain astronomy
community in data analysis, visualisation, collaboration and coordination.
The live fritz.science instance is a specific implementation of Skyportal designed to
serve the ZTF-II partnership, supporting and enabling scientific discovery.

However, there are constraints which will limit the performance and capability of Fritz.
The infrastructure to operate Fritz exists in the cloud but costs real money,
and therefore a tradeoff must be made between user experience and available resources.
We only have 24 instances of Fritz, each running on a dedicated CPU core,
equivalent to ~2 MacBook Pros. With these resources, we need to provide website access
to many users while querying a database of ~1Tb and running extra services such as
generating optimal ZTF schedules. Moreover, Skyportal is not developed by professional
contracted software developers, but rather by a small team of scientists who contribute
their own time. This time is also not limitless. Development in Skyportal relies on
active and interactive community feedback to identify missing features and to inform
prioritisation between multiple competing requests. Unfortunately there is not enough
developer time to go around (though you can always consider volunteering YOUR time to
ensure the features you need are available!).

With our vision and constraints in mind, this document aims to provide guidelines to
ensure fair use across the ZTF collaboration. The limited resources make this, in some
sense, a zero sum game. Excessive demand by one user can inadvertently impact the
provision for many others.

Our first and most important request is that **users behave responsibly**!
Be a civic-minded scientist, and remember that your actions may impact your
collaborators. So please do not shoot first and then ask questions later.
If you wish to use Fritz in a new way, or to substantially scale up something that
you tested on your laptop with only a handful of sources, come and ask us about it.
We want to have an idea of how users interact with Fritz, and we might even have
suggestions for doing it more quickly and efficiently.

Some other things to bear in mind:

We can’t fix problems if we do not know about them. Please report problems on the Fritz
Slack channels, and also record specific bugs or requests by creating an “Issue” on the
Skyportal Github page: https://github.com/skyportal/skyportal/issues.
Recording the exact time you faced an issue is helpful,
as well as any extra details you can provide.

Poorly constructed API calls have substantially more chaotic potential than
GUI interactions. Automated python scripts can easily bring down Fritz.
You should always wait at least a second between API calls.
Don’t just endlessly retry failed queries without pause
(30s is a good minimum delay time between attempts),
please eventually give up and concede defeat if your query fails repeatedly,
and consider using a package like backoff (https://github.com/litl/backoff)
to regulate requests. You can see an example :ref:`here <api_examples>`.

**As a rule of thumb, if your request involves “>100” of anything, it is “big”.
Please talk to us first!**

We track usage based on API tokens, enabling us to diagnose troublesome API calls
which impact Fritz stability. Please don’t share tokens, because then we cannot easily
map requests to users. If you are doing multiple “big” things, each one should really
have its own token. Please contact us, and we can provide additional tokens.

Not all API calls are created equal. Consider the “cost” of the calls you are making,
and whether they can be reduced. Our total operating costs are >$2000 just to cover
cloud computing. When it comes to the cost of transferring data, “less is more”.
So, using the API to pull metadata, spectra and cutouts for a source will be much more
expensive than just pulling the name and classification. Please don’t pull more data
than you need to!

If you want a program to run every day, you should not be requerying for data that you
already received yesterday, last week, or last year. Please take some time to save data
locally if you can. Fritz is not intended to be your personal external hard drive.


