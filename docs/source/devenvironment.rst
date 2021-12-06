==========================================
How to Set-up Your Development Environment
==========================================

Now that you have read the Requirements, Testing Plan, and Potential
Mockups for `Command Line Tic-Tic-Toe </source/releases/commandline>`_, let's begin to code it together.
The first thing you will need to do--only for the first Release--is 
to set-up your development environment. You are welcome to use any 
environment you like, but software architecture includes planning for 
how code will be versioned, deployed, and debugged, so we have a plan 
for you. A great architecture might also include a coding style guide 
like the one at https://google.github.io/styleguide/pyguide.html. 
We'll just point you to that one.

Here's a summary of our plan:

1. Set up a **GitHub** account, and clone the redscience template to get 
   the initial set-up.
2. Set up a **Google** account.
3. In **Google Colab**, mount your Google Drive, then clone your GitHub 
   repository ("repo") to your Google Drive where you can edit and run your 
   code in the cloud.
4. Test your revisions with pytest and linters, then commit them to GitHub
5. (Optional) Set up a **ReadTheDocs** account and link it to your GitHub 
   repo to automatically generate documentation.
6. (Optional) Set up a **PyPI** account and link it to your GitHub repo 
   to share your code with the world.

This article will walk you through step 1, explain what you have inherited 
by cloning the template, then point you to other resources that 
cover later steps.

How to Choose Development Tools
-------------------------------

You don’t have to use GitHub, Colab, ReadTheDocs, and PyPI. This section 
highlights some of the features you might look for in replacements. Feel
free to skip this section if you simply want to adopt the provided 
architecture.
 
You are about to build something, and you will master it in the process. 
You might expect to discard your work at that point and take away only 
memories. But it is also possible that you might want to continue evolving 
what you built, maybe even transform it into something with a very 
different purpose. Just in case that happens, the provided architecture 
includes best practices for general development. 

Note that evolving a competitor for redscience is not what we have in mind 
by "continue evolving what you built". If you want to improve redscience, 
then please offer a pull request to it so everyone can enjoy your 
innovation. If your improvement is rejected, then it would be better to 
fork redscience (and poach from its community) than to rebuild it 
completely. If you want to customize redscience, then merely wrap it, so 
your customized version will automatically enjoy any future improvements 
to redscience. What we have in mind by "continue evolving what you built" 
is to copy patterns or chunks of what you built to your next project. The 
best kind of code to reuse is (a) code you understand (which you will, 
since you built it), and (b) code built to last. 

If you want to build software to last, you should expect it to need a 
community to provide security updates as security vulnerabilities become 
discovered, compatibility updates as dependencies evolve (e.g. operating 
systems, storage systems, and browsers), and new features as user 
expectations shift (e.g. to different devices). At first, you might 
be the only member of your community, or every member might be an employee 
of a single business, government or religion, but building code to last 
means designing it to extend beyond that. Even if many people want to 
participate in a such a community, the community will need the following:

* Development environments (including hardware), 
* Means to transfer knowledge to new members (i.e. documentation/training), 
* Means to set priorities/resolve disagreements (i.e. management), 
* Means to control quality (i.e. testing), and 
* Means to connect with the needs of users (i.e. sales/implementation 
  and issue reporting framework)
 
Not only must your software be able to evolve over time, so must these 
resources. The hardware your community will need to maintain your software 
20 years from now might be very different from the hardware required today. 
This is where **Colab** comes in. Rather than plan to buy new hardware every 
so often to support your software, you can develop “in the cloud” and let 
the cloud provider handle upgrading the hardware. It is important that 
whichever provider you choose is (1) accessible to your community, (2) 
provides reliable quality hardware, and (3) is compatible with the rest 
of your development environment. Colab is accessible for free (up to 
certain limits) to anyone with a web browser (e.g. cell phone), and it 
provides very fast GPUs. Most of the Jupyter Notebooks development 
environment on Colab can be made available elsewhere—it provides as many 
cells as you like in which to experiment—but Google added 
autocomplete and help windows that are noteworthy features.
 
Similarly, your community 20 years from now might need new ways to 
transfer knowledge about how to maintain it. It helps that the Python 
language is relatively easy to read. Yet, the current state-of-the-art in 
knowledge-transfer also includes providing documentation (both in code and 
out of code). The current Python standard is to write documentation in 
reStructuredText (RST) built with Sphinx (via **ReadTheDocs**). This 
is not effortless--your community would need to abide documentation 
standards and would need educators to write everything beyond the 
API--but automation saves effort on converting documentation between forms 
to permit browsing, searching, and printing (e.g. to html and pdf). You 
could give your software a fancy website without RST (but it would still 
take effort), and RST can’t embed functioning Jupyter Notebooks (like it 
can videos), but would your coders and writersend-up at each other's throats
if you didn't have a searchable instruction manual that automatically-updates 
the API sections whenever the code changes? 
Linking to ReadTheDocs is an optional step in this curriculum, but the 
architecture models corresponding documentation standards (to keep that 
documentation option viable).
 
Your community 20 years from now also might not be able to set 
priorities and resolve disagreements the way it can now. Benevolent dictators 
do not last forever. Furthermore, better processes for achieving consensus 
may evolve over time, and you will automatically benefit from those 
innovations if you use a leading code-management system. ReadTheDocs 
currently integrates with GitHub, BitBucket, and GitLab, of which **GitHub** 
is currently the most popular. All three innovate processes to manage code 
communally, including ways to report issues. One of their most important 
innovations is the “Pull request” (or “Merge request”) which overcomes 
natural-resistance-to-change by empowering a developer to propose a code 
change in a way that makes it easy for others to analyze and test (even 
automatically), try, debate, and accept. GitHub can automatically generate 
pull requests whenever dependencies upgrade and automatically inform you 
if proposed changes would break functionality or introduce security 
vulnerabilities.
 
Finally, although code-management systems provide means to benefit from 
a community, they don’t necessarily attract that community. The ways in 
which people form communities may change over the next 20 years, but 
bulk-searches through “what’s out there” will likely be part of the mix. 
**PyPI** is python’s standard index, so it is a natural place for a 
bulk-search. Users may not need to use PyPI to install your software 
if they can run it “in the Cloud” via Colab, but being indexed in PyPI may 
be crucial to being discoverable. Linking to PyPI is an optional step in 
this curriculum, but the package is set up to permit it.

How to Set-up on GitHub
-----------------------

First, if you don't already have a GitHub account, follow 
`the GitHub instructions <https://docs.github.com/en/get-started/signing
-up-for-github/signing-up-for-a-new-github-account>`_
to get one. 

If this is a group project with an existing repository, then fork it.
If you want to start a new code base, then the plan is to start by 
clicking "Use this template" at 
https://github.com/ChrisSantosLang/redscience (instructions from
GitHub `here <https://docs.github.com/en/github/creating-cloning-and-
archiving-repositories/creating-a-repository-on-github/creating-a-
repository-from-a-template>`_)

[Describe folder structure and explain configuration files here]

How to Set-up Colab
-------------------
 
At this point, you should have your own GitHub repo for this project. 
If you don't already have a Google account, follow 
`the Google instructions <https://support.google.com/accounts/answer/27441?hl=en#>`_ 
to get one, then move forward to How to Develop in Colab with GitHub. 
