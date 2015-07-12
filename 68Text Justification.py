##Text Justification
##
##2015年7月10日  AC
##zss

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        groups,group =[],[]
        width = 0
        for word in words:
            width += len(word)
            if width + len(group) > maxWidth:
                pos = len(group) if len(group)==1 else len(group)-1
                space = (maxWidth-width+len(word))//pos
                spaceLeft =  (maxWidth-width+len(word))% pos
                for i in range(1,2*pos,2):
                    if spaceLeft:
                        group.insert(i,' '*(space+1))
                        spaceLeft -= 1
                    else:
                        group.insert(i,' '*(space))
                groups.append(group)
                group = []
                width = len(word)
            group.append(word)
        pos = len(group) if len(group)==1 else len(group)-1
        space = (maxWidth-width)
        for i in range(1,2*pos,2):
            if space:
                group.insert(i,' ')
                space-=1
        group.insert(len(group),' '*space)
        groups.append(group)
        return [''.join(groups[i]) for i in range(len(groups))]
        
