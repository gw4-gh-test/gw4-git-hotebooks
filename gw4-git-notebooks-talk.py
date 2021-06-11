# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"}
# <h1><center>GW4 BioMed NMH Theme Session 2021</center></h1>
# <h1><center>Open reproducibility tools - git and lab notebooks</center></h1>
# <h3><center>Mark Einon, Systems Manager</center></h3>
# <h3><center>DPMCN / Centre for Neuropsychiatric Genetics &amp; Genomics</center></h3>
# <h3><center>Cardiff University</center></h3>
# <h3><center>einonm@cardiff.ac.uk</center></h3>

# + slideshow={"slide_type": "-"} active=""
# <script>
#   $( document ).ready(function(){
#     <!--$('div.input').hide()-->
#     $('div.prompt').hide()
#   });
#   
# </script>

# + [markdown] slideshow={"slide_type": "slide"}
# ### Why has the talk title changed ?
#
# * Github and Rmarkdown are two of many tools that facilitate open reproducibility
#     * AS important to know why they are used than how to use them
#     * The tools used will change between projects and over your career
#
#
# * Github is a fancy way of displaying information from the git tool
#     * Git is a command line tool, where the real power & usefulness lies 
#     * Another similar alternative to Github is the open source Gitlab
#
#
# * Rmarkdown is specific to the R language, Jupyter Notebooks also exist for R, python and dozens of other langs
#     * Both are empowered by git and can be used as data science lab notebooks

# + [markdown] slideshow={"slide_type": "slide"}
# # What is Open Reproducible Research?
#
# <img src="./Os_taxonomy.png" style="float: centre; width: 10260px; height: 540px;">
#
# <small>https://www.fosteropenscience.eu</small>

# + [markdown] slideshow={"slide_type": "slide"}
# # What is Open Reproducible Research? (Cont.)
#
# Open science involves making scientific methods, data, and outcomes available to everyone. It can be broken down into several parts, including:
#
# * Transparency in data collection, processing and analysis methods, and derivation of outcomes.
# * Publicly available data and associated processing methods.
# * Transparent communication of results..
#
# Reproducible science is when anyone (including others and your future self) can understand and perform the steps of an analysis, applied to the same or even new data - achieving the same results.
#
# Together, open reproducible science results from open workflows that allow you to easily share work and collaborate with others as well as openly publish your data and workflows to contribute to greater scientific knowledge.
#
#
# <small> From https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/get-started-open-reproducible-science/</small><br>
# <small>Also see https://lgatto.github.io/open-and-rr-2/</small>

# + [markdown] slideshow={"slide_type": "slide"}
# # Why is open reproducible research being encouraged?
#
# * A **replication crisis** has been found to exist and open science is seen as a solution, of which open reproducible research is a part.
#
#
# * Many findings were found to be doubtful [1], due to: 
#     * Generation of new data/publications at an unprecedented rate.
#     * Compelling evidence that the majority of these discoveries will not stand the test of time.
#     * **Causes: failure to adhere to good scientific practice and the desperation to publish or perish**
#     * This is a multifaceted, multi-stakeholder problem.
#     * No single party is solely responsible, and no single solution will suffice.
#     
# <small>1. https://en.wikipedia.org/wiki/Replication_crisis</small>

# + [markdown] slideshow={"slide_type": "slide"}
# # The story so far...
#
# * For a long time, it has been possible to be a top researcher in the field without ever having shared working, reliable code.
#
# * Funders would still give you money
# * Publishers would still publish without working code
# * Peer reviewers would not insist on having verifiable code
# * Unlikely that anyone would ask to repeat your findings using your scripts (also easy to fob off)
# * PhDs happen without this sort of collaboration - the code probably wasn't reviewed, shared or run by anyone else, so the relevant collaboration skills are not taught.

# + [markdown] slideshow={"slide_type": "slide"}
# # The situation is changing...
#
# Researchers are being increasingly challenged to practice open science that goes beyond open access and open data, extending all the way to making software and data research outputs truly repeatable and reproducible.
#
# Funders[1], journals[2] and REF[3] are making strong recommendations and sometimes mandatory policy to instil an open science culture and adopt practices successfully established in open source communities, and the rate of such activities is increasing.
#
# These practices aim to ensure defect-free behaviour of software which is understandable by other researchers and produce results using repeatable pipelines.
#
# <small>1. https://wellcome.org/grant-funding/guidance/how-complete-outputs-management-plan</small><br>
# <small>2. https://www.nature.com/documents/GuidelinesCodePublication.pdf</small><br>
# <small>3. https://www.ukri.org/our-work/supporting-healthy-research-and-innovation-culture/open-research/</small>

# + [markdown] slideshow={"slide_type": "slide"}
# ## Meeting open reproducible research requirements
#
# Open reproducible research is increasingly becoming a requirement to obtain funding and publish research. To ensure open reproducible research, we may need to provide:
#
# <img src="./hamilton1.jpg" style="display: block; float: right; width: 260px; margin-left: 10px; margin-right: 10px;">
#
# * Source code
# * Documentation
# * Executables
# * Software dependencies
# * Narratives of what the code is doing 
# * Narratives of whole workflows
# * Input and output data
# * Open licensing
#
# <small>1. https://www.software.ac.uk/blog/2018-05-22-sharing-reproducible-research-minimum-requirements-and-desirable-features</small>

# + [markdown] slideshow={"slide_type": "slide"}
# # Git
#
# * Git is a version control & complex communication tool that is the bread-and-butter of data science best practice
#     * An industry-standard tool
#
# * It is essentially a command line tool with other web-based interfaces available, e.g. GitHub & GitLab
#
# * Git fluency is currently a basic necessity for producing reproducible data science
#
# * It is quick to understand and use basic git features, but does have a learning curve for more powerful features
#     * every change to a set of text-based files has it's own ID and log message
#     * ability to revert to any previous version or see differences between versions
#     * gtilab/github give free, online cloud storage for your code
#     * easier to get support in tackling issues in your project

# + [markdown] slideshow={"slide_type": "slide"}
# # Learning git
#
# * Software Carpentry have a well-pitched comprehensive introductory course at https://swcarpentry.github.io/git-novice/ (3-4 hrs)
#
# * Git is a tool (mechanism) and doesn't dictate a process (policy) to use it.
#
# * Git can be used by a sole developer, a team or an entire community
#
# * Always choose/define a process! Having a best-practice process has a greater bearing on quality than the people
#     * Code peer review is the next most fruitful best practice a project could adopt
#     
# * Git is like chess, rules easy to learn but competency comes from practising
#     
# * https://sdlambert.github.io/2015/04/09/git-workflow-for-solo-development/ git workflow for solo development
# * https://osf.io/4yp9a/?action=download Curating Research Assets: A Tutorial on the Git Version Control System
# * https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project GitHub - contributing to a Project
# * https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510 Good enough practices in scientific computing

# + [markdown] slideshow={"slide_type": "slide"}
# # Example sole developer git workflow
#
# ### Setup a local repository with a remote copy
#
# * Initialise a local git repository
# * Create a remote repository 
# * Create a git repo README.txt & LICENCE.txt
# * Add the README, LICENCE and any existing files to the local repository, ensuring the git commit message follows best practice
# * Push the local committed changes to the remote repository
#
# ### Make and version a change 
#
# * Edit some files in the local repository, making changes to do one complete, logical thing only. E.g. fix a bug, add a feature or some tests
# * Test the changes, ensuring the code runs with no regressions
# * Add the new file modifications to the local repository, ensuring the git commit message follows best practice
# * Push the local committed changes to the remote repository
#
# ### Make a big change 
#
# * Create a git branch in which to develop the desired change
# * Make and commit several logical changes to develop the big change
# * Test the big change, ensuring the code runs with no regressions
# * Rebase branch onto the HEAD of master
# * Push the local committed changes to the remote repository
#
# #### Team workflow
#
# * This would use branches more extensively and adopt peer review as a gateway to getting changes merged into the shared branch/repository

# + [markdown] slideshow={"slide_type": "slide"}
# # Data science notebooks
#
# * These are plain-text documents that mix markdown narrative with code and optionally the code output, which is often graphs and tables
#
# * They are split into a series of 'cells' of markdown or code. The code can be executed in-situ and exported to html, pdf, slideshows, dashboards and other formats.
#
# * Jupyter notebooks 
#
# * Rmarkdown is technically non-interactive, but the newer R notebooks add this functionality to mimic Jupyter notebooks in this regard - so that cells can be edited and run in the same document.
#
# * These slides were created in a Jupyter Notebook
#     
#
# https://www.datacamp.com/community/blog/jupyter-notebook-r
# https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook

# +
## Markdown


# -

# demos: 
#     * setting up a git repo. Psuhing to gitlab/pushing to github
#     * Creating an Rmarkdown doc and pushing to the repos
#     * Creating a jupyter notebook and pushing to the repos
#     
# * or create a typo on here and fix it...
#

# + [markdown] slideshow={"slide_type": "slide"}
# ## best practices - what changes could be adopted?
#
# * Removing manual analysis steps - put into code form and automated
#
# * Version control of code & associated documents (e.g. licence/guides) - used by all project members
#
# * Shared and discoverable workflows/code - division gitlab group
#
# * 'Agile' checklists, guides and workflow documentation - light touch and generic
#
# * Training - including learning from participation & outputs of others
#
# * Pipeline validation & testing
#
# * Project issue trackers
#
# * Peer review of code
#
# * Ensuring feedback loops exist to improve practices - development processes are projects themselves
#
# * Fostering a community of practitioners

# + [markdown] slideshow={"slide_type": "notes"}
# * Not saying that the practices are not currently being carried out, but are on an ad-hoc basis
# * The practices do not necessarily make things faster, but reduce the uncertainty in the amount of time things take and of the reliability of artefacts produced
# * Partaking in these practices themselves is a training exercise
# * This is not an academic-led subject, more vocational, led by practising

# + [markdown] slideshow={"slide_type": "slide"}
# ## Summary
#
# * We have several challenges in data science that threaten our success
# * To tackle the issues identified, we'll need to adopt some new practices
# * These practices are collaborative, whereas our current practitioners are mainly siloed
# * The implied change of culture requires top management backing
# * A divisional strategy is an important part of this backing
#
# "We aim to have a world leading capability for analysing neuroscientific, genomic & phenotypic data by fostering a data science environment that supports our planning, reproducibility, reliability and complexity needs"

# + [markdown] slideshow={"slide_type": "notes"}
# * Thanks to Nigel Williams & peter Holmans for their advice
# * This is an opinionated wishlist from my personal experience - other views are available
# * Courses are great at covering basics - but not an academic-led subject, more vocational & led by practitioners
# * This works phenomenally well in the open source / commercial world, and they reap the benefits - we won't be able to reap the technology benefits without a culture that's set up to do so!
# * No strategy survives a meeting with reality!
