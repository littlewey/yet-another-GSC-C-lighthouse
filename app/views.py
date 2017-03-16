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
    developerID = models.Developer.query.filter_by(NameString = developerName).first().id
    toolID = models.Developer_tool_map.query.filter_by(developer_id = developerID)
    if serviceArea.startswith('all'):
        pagination = models.Tool.query.filter_by(models.Tool.developer_tool_mapping.has(models.Tool.developer_tool_mapping.developer_id==developerID)).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    else:
        pagination = models.Tool.query.filter_by(models.Tool.developer_tool_mapping.has(models.Tool.developer_tool_mapping.developer_id==developerID)).filter_by(ServiceArea=serviceArea).order_by(models.Tool.DownloadTimes.desc()).paginate(page, per_page=TOOLS_PER_PAGE, error_out = False)
    tools = pagination.items
    return render_template("developer.html",
                           developer=developer,
                           toolScope=tools,
                           pagination=pagination,
                           tabs=tabs,
                           endpoint='developer',
                           serviceArea= serviceArea,
                           SiteNameString=SiteNameString
                           )
