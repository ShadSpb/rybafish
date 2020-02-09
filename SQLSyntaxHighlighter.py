from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor
from PyQt5.QtCore import Qt, QRegExp, QRegularExpression

import re
#from PyQt5.QtCore import Qt

class SQLSyntaxHighlighter(QSyntaxHighlighter):

    def highlightBlock(self, text):
    
        fmKeyword = QTextCharFormat()
        fmKeyword.setFontWeight(QFont.Bold)
        fmKeyword.setForeground(QColor('#808'))

        fmComment = QTextCharFormat()
        fmComment.setForeground(QColor('#080'))

        fmLiteral = QTextCharFormat()
        fmLiteral.setForeground(QColor('#00F'))
        
        keywords = ['select', 'from', 'order', 'by', 'group', 'where', 'inner', 'left', 'right', 'join', 'as',
                    'where', 'asc', 'desc', 'case', 'when', 'else', 'and', 'or', 'like', 'round']

        rules = []

        '''
        for kw in keywords:
            rules.append([QRegularExpression('\\b'+kw+'\\b'), fmKeyword])
            
            
        # literals
        #rules.append([QRegularExpression('\'[^\']*\''), fmLiteral])
        rules.append([QRegularExpression('\'.+?\''), fmLiteral])

        rules.append([QRegularExpression('".+?"'), fmLiteral])

        # one line comment
        rules.append([QRegularExpression('--.+'), fmComment])

        for r in rules:
            (rule, format) = (r[0], r[1])
            mi = rule.globalMatch(text)
        
            while mi.hasNext():
                m = mi.next()
                self.setFormat(m.capturedStart(), m.capturedLength(), format)
                
        '''
        
        for kw in keywords:
            git.append(['\\b'+kw+'\\b', fmKeyword])

        # one line comment
        rules.append(['--.+', fmComment])
        
        # literals
        rules.append(['\'.+?\'', fmLiteral])
        rules.append(['".+?"', fmLiteral])
        
        for r in rules:
            (pattern, format) = (r[0], r[1])

            m = re.search(pattern, text, re.Igit )
        
            #just one possible?
            if m is not None:
                self.setFormat(m.start(0), len(m.group(0)), format)

        '''
        # multiline comments
        # https://doc.qt.io/qtforpython/PySide2/QtGui/QSyntaxHighlighter.html
        
        commStart = 0
        
        if self.previousBlockState() != 1:
            mi = QRegularExpression('/\\*').globalMatch(text)
            if mi.hasNext():
                commStart = m.capturedStart()
                
        while commStart >= 0:
        '''