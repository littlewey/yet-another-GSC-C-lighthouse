from flask import render_template, g, redirect, url_for
from app import app
from app import models
from config import TOOLS_PER_PAGE
from forms import SearchForm
from config import MAX_SEARCH_RESULTS, SiteNameString, tabs


@app.route('/search', methods = ['POST'])
def search():
    search_form = SearchForm()
    g.search_form = search_form
    #print g.search_form.search.data
    return redirect(url_for('search_results', query = g.search_form.search.data , page = 1, serviceArea ='all_serviceArea'))

@app.route('/search_results/<serviceArea>/<query>/<int:page>')
def search_results(query,serviceArea='all_serviceArea', page = 1):
    #print query
    if serviceArea.startswith('all'):
        pagination = models.Tool.query.whoosh_search(query, MAX_SEARCH_RESULTS).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    else:
        pagination = models.Tool.query.filter_by(ServiceArea=serviceArea).whoosh_search(query, MAX_SEARCH_RESULTS).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)

    #print pagination
    results = pagination.items
    #print results
    return render_template('index.html',
        query = query,
        title=query + " search results",
        toolScope = results,
        pagination = pagination,
        tabs = tabs,
        endpoint='search_results',
        serviceArea=serviceArea,
        SiteNameString=SiteNameString
        )

@app.route('/', methods = ['GET', 'POST'])
@app.route('/tool', methods = ['GET', 'POST'])
@app.route('/tool/<serviceArea>/<query>/<int:page>', methods = ['GET', 'POST'])
def tool(page = 1, serviceArea= 'all_serviceArea',query='all' ,SiteNameString=SiteNameString):
    if serviceArea.startswith('all'):
        pagination = models.Tool.query.order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    else:
        pagination = models.Tool.query.filter_by(ServiceArea=serviceArea).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    tools = pagination.items
    #print tools
    return render_template("index.html",
                            toolScope=tools,
                            pagination=pagination,
                            tabs=tabs,
                            endpoint='tool',
                            serviceArea= serviceArea,
                            SiteNameString=SiteNameString
                            )
@app.route('/developer', methods = ['GET','POST'])
@app.route('/developer/<serviceArea>/<developerName>/<int:page>', methods = ['GET','POST'])
def developer(developerName, page = 1, serviceArea= 'all_serviceArea', SiteNameString=SiteNameString):
    if serviceArea.startswith('all'):
        pagination = models.Tool.query.whoosh_search(developerName, fields=('DeveloperList',)).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    else:
        pagination = models.Tool.query.whoosh_search(developerName, fields=('DeveloperList',)).filter_by(ServiceArea=serviceArea).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    tools = pagination.items
    return render_template("developer.html",
                           developerName=developerName,
                           toolScope=tools,
                           pagination=pagination,
                           tabs=tabs,
                           endpoint='developer',
                           serviceArea= serviceArea,
                           SiteNameString=SiteNameString,
                           title = 'Tools created by '+developerName
                           )

@app.route('/keyword', methods = ['GET','POST'])
@app.route('/keyword/<serviceArea>/<keywordName>/<int:page>', methods = ['GET','POST'])
def keyword(keywordName, page = 1, serviceArea= 'all_serviceArea', SiteNameString=SiteNameString):
    if serviceArea.startswith('all'):
        pagination = models.Tool.query.whoosh_search(keywordName, fields=('KeyWordList',)).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    else:
        pagination = models.Tool.query.whoosh_search(keywordName, fields=('KeyWordList',)).filter_by(ServiceArea=serviceArea).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    tools = pagination.items
    return render_template("keyword.html",
                           keywordName=keywordName,
                           toolScope=tools,
                           pagination=pagination,
                           tabs=tabs,
                           endpoint='keyword',
                           serviceArea= serviceArea,
                           SiteNameString=SiteNameString,
                           title = 'Keyword: '+keywordName
                           )
@app.route('/wiki', methods = ['GET','POST'])
def wiki():
    return render_template("wiki.html",
                           endpoint='wiki',
                           SiteNameString=SiteNameString,
                           title = 'Search Innodex',
                           )

