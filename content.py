# Text content of static pages
# Extract as python file, for easy maintain
# Created by olala7846@gmail.com

index_content = {
    'about': """
        I'm a newbie full-stack web developer from Taiwan, currently undergoing my full-stack development nanodegree at <a href="https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004">Udacity</a>. before that I was an iOS + Backend engineer at <a href="https://livehouse.in/">LIVEhouse.in</a>. My favoriate programming language is <img src="/static/img/python-logo.png" class="text-height">Python and my favoriate web platform is <a href="https://cloud.google.com/appengine/"><img src="/static/img/gaelogo.png" class="text-height">Google App Engine</a>. I will finish my course soon, wish we luck!
    """,
    'skills': [
        ('Languages', [
            ('Python', '/static/img/python-logo.png'),
            ('Node.js', '/static/img/nodejs-logo.png'),
            ('HTML5', '/static/img/html-logo.png'),
            ('Objective C', '/static/img/objc-logo.png')
        ]),
        ('Frameworks', [
            ('Google App Engine', '/static/img/gaelogo.png'),
            ('Flask', '/static/img/flask.png'),
            ('Jinja', '/static/img/jinja-logo.png')
        ]),
        ('Database', [
            ('Google Cloud Datastore', '/static/img/datastore-logo.png'),
            ('PostgreSQL', '/static/img/psql-logo.png'),
            ('MongoDB', '/static/img/mongodb.png')
        ])
    ],
    'experiences': [
        {
            'title': 'Full-stack Web Developer',
            'time': '2015 ~ now',
            'icon': 'filter_drama',
            'detail': """
               Voting system<br>
               - Developed frontend + backend for <a href="http://ntuvb-allstar.appspot.com/index">NTU all-start volleyball game</a> with Google App Engine.
            """
        },
        {
            'title': 'Backend Engineer',
            'time': '2012~2015',
            'icon': 'settings',
            'detail': """
                Backend Engineer at LIVEhouse.in<br>
                - Provides JSON api for mobile app and implements shared internal npm packages.<br>
                - Reduced storage cost by 20%~50% using <a href="https://cloud.google.com/storage/docs/nearline?hl=en">Google nearline storage</a>.
            """
        },
        {
            'title': 'iOS Engineer',
            'time': '2012~2015',
            'icon': 'stay_primary_portrait',
            'detail': """
                iOS Developer at LIVEhouse.in<br>
                - <a href="https://itunes.apple.com/tw/app/livehouse.in/id912290138?mt=8">App</a> engineer in a team of three. responsible for structural design and library survey. Initiated <a href="http://google.com/chromecast">Chromecast</a> support, introduced <a href="http://www.google.com/analytics/ce/nrs/tag-manager/">Google Tag Manager</a> library.<br>
                - Built up continuous integration system with Jenkins, Gitlab Webhook, XCTest/OCMock, HockyApp API.<br>
                - Face to face interviewd 20+ candicates.
            """
        },
    ]
}
