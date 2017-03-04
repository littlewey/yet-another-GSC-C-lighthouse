from app import db

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ServiceArea = db.Column(db.String(16), index = True, unique = False)
    NameString = db.Column(db.String(64), index = True, unique = False)
    DeveloperList = db.Column(db.String(256), index = True, unique = False)
    KeyWordList = db.Column(db.String(512), index = True, unique = False)
    InnovatorName = db.Column(db.String(256), index = True, unique = False)
    Description = db.Column(db.String(65535), index = True, unique = False)
    ToolUrlOnLightHouse = db.Column(db.String(256), index = True, unique = False)
    Rates = db.Column(db.Float(8), index = True, unique = False)
    DownloadTimes = db.Column(db.Integer, index = True, unique = False)
    ImplementedDate = db.Column(db.String(64), index = True, unique = False)
    developer_tool_mapping = db.relationship('Developer_tool_map', backref='tool', lazy='dynamic')
    keyword_tool_mapping = db.relationship('Keyword_tool_map', backref='tool', lazy='dynamic')

    def __repr__(self):
        return '<Tool %r>' % (self.NameString)

class Developer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    NameString = db.Column(db.String(32), index = True, unique = False)
    developer_tool_mapping = db.relationship('Developer_tool_map', backref='developer', lazy='dynamic')

    def __repr__(self):
        return '<Developer %r>' % (self.NameString)

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    NameString = db.Column(db.String(32), index = True, unique = False)
    keyword_tool_mapping = db.relationship('Keyword_tool_map', backref='keyword', lazy='dynamic')

    def __repr__(self):
        return '<Keyword %r>' % (self.NameString)

class Developer_tool_map(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'))

    def __repr__(self):
        return '<Developer_tool_map %r>' % (str(self.id))

class Keyword_tool_map(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'))
    keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'))

    def __repr__(self):
        return '<Keyword_tool_map %r>' % (str(self.id))




