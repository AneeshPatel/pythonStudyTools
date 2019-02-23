class Topics(object):
    def __init__(self, pointlineandplane, postulates, shapes, properties, theorems, ifthenstatements, corallaries):
        self.pointlineandplane=pointlineandplane
        self.postulates=postulates
        self.shapes=shapes
        self.properties=properties
        self.theorems=theorems
        self.ifthenstatements=ifthenstatements
        self.corallaries=corallaries

pointlineandplane2=["Through any 2 points", "A line contains at least", "If 2 lines intersect", "Through any 3 non-collinear points", "If 2 points lie in a plane", "When 2 planes intersect", "Distance from a point to a line", "Distance between 2 parallel lines"]
pointlineandplane={"Through any 2 points" : "there exists exactly one line", "A line contains at least" : "2 points", "If 2 lines intersect" : "then their intersection is exactly one point ", "Through any 3 non-collinear points" : "there exists exactly 1 plane", "If 2 points lie in a plane" : "then the line containing them lies in the plane", "When 2 planes intersect" : "then their intersection is a line", "Distance from a point to a line" : "the length of the perpendicular segment from the point to the line. The perpendicular segments is the shortest distance between the point and the line", "Distance between 2 Parallel Lines" : "It is the length of any perpendicular segments joining the 2 lines"}
postulates2=["Ruler Posulate","Segment Addition Postulate","Protractor Postulate","Angle Addition Postulate","Linear Pair Postulate","Parallel Postulate","Perpendicular Postulate"]
postulates={"Ruler Posulate" : "The points on a line can be matched on to one with the real numbers. The real numbers that corresponds to a point is the coordinate of the point. (how to use a ruler)", "Segment Addition Postulate" : "If B is between A and C, then AB+BC=AC. If AB+BC=AC, then B is between A and C.", "Protractor Postulate" : "The rays of an angle can be matched with real numbers from 0-180", "Angle Addition Postulate" : "If line P is in the interior of ∠RST, then the measure of ∠RST is equal to the sum of ∠RSP and ∠PST", "Linear Pair Postulate" : "If 2 angles form a linear pair, then they are supplementary", "Parallel Postulate" : "If there is a line and a point not on the line, then there is exactly one line through the point parallel to the given line", "Perpendicular Postulate" : "If there is a line and a point not on the line, then there is exactly one line through the point perpendicular to the given line"}
shapes2=["Circle","Triangle","Square","Rectangle"]
shapes={"Circle" : "Diameter - d and Radius - r \nCircumference = 2πr or 2πd \nArea = πr²", "Triangle" : "Side Lengths - x,y,z Base - b and Height - h \nPerimeter = x+y+z \nArea = 1/2bh", "Square" : "Side Length - s \nPerimeter = 4s \nArea = s²", "Rectangle" : "Length - l and Width - w \nPerimeter = 2l+2w \nArea = lw"}
properties2=["Addition Property of Equality","Subtraction Property of Equality","Multiplication Property of Equality","Division Property of Equality","Substitution Property of Equality","Distributive Property","Reflexive Property of Equality","Reflexive Property of Equality","Reflexive Property of Equality","Symmetric Property of Equality","Symmetric Property of Equality","Symmetric Property of Equality","Transitive Property of Equality","Transitive Property of Equality","Transitive Property of Equality"]        
properties={"Addition Property of Equality" : "If a=b, then a+c=b+c", "Subtraction Property of Equality" : "If a=b, then a-c=b-c", "Multiplication Property of Equality" : "If a=b, then ac=bc", "Division Property of Equality" : "If a=b and c≠0, then a÷c=b÷c", "Substitution Property of Equality":"If a=b, then a can be substituted for b in any equation or expression", "Distributive Property":"a(b+c)=ab+ac","Reflexive Property of Equality":"For any real number a, a=a", "Reflexive Property of Equality":"For any segment AB, AB=AB","Reflexive Property of Equality":"For any angle A, m∠A=m∠A", "Symmetric Property of Equality":"For any real numbers a and b, if a=b, then b=a","Symmetric Property of Equality":"For any segments AB and CD, if AB=CD, then CD=AB", "Symmetric Property of Equality":"For any angles A and B, if m∠A=m∠B, then m∠B=m∠A", "Transitive Property of Equality":"For any real numbers a,b and c, if a=b and b=c, then a=c", "Transitive Property of Equality":"For any segments AB, CD, and EF, if AB=CD and CD=EF, then AB=EF", "Transitive Property of Equality" : "For any angles A, B and C, if m∠A=m∠B and m∠B=m∠C, then m∠A=m∠C"}        
theorems2=["Right Angle Congruence Theorem","Congruent Supplements Theorem","Congruent Complements Theorem","Verticals Angles Congruence Theorem","Converse of Correspnding Angles Theorem","Alternate Interior Angles Theorem","Alternate Exterior Angles","Consecutive Interior Angles Theorem","Converse of the Alternate Interior Angles Theorem","Converse Exterior Angles Theorem","Converse of Consecutive Interior Angles Theorem","Perpendicular Transversal Theorem","Lines Perpendicular to a Transerval Theorem","Triangle Sum Theorem","Exterior Angles Theorem","Base Angles Theorem","Converse of the Base Angles Theorem"]
theorems={"Right Angle Congruence Theorem" : "All right angles are congruent" , "Congruent Supplements Theorem" : "If 2 angles are supplementary to the same angle (or to congruent angles), then they are congruent", "Congruent Complements Theorem" : "If 2 angles are comlementary to the same angle (or to congruent angles), then they are congruent", "Verticals Angles Congruence Theorem" : "Vertical angles are congruent", "Converse of Correspnding Angles Theorem" : "If 2 angles are cut by a treansversal so that the corresponding angles are congruent, then the lines are parallel", "Alternate Interior Angles Theorem" : "If 2 parallel lines are cut by a transversal, then the pairs of alternate interior angles are congruent", "Alternate Exterior Angles" : "If 2 parallel lines are cut by a transversal, then the pairs of alternate exterior angles are congruent", "Consecutive Interior Angles Theorem" : "If 2 parallel lines are cut by a transversal, then the pair of consecutive interior angles are supplementary", "Converse of the Alternate Interior Angles Theorem" : "If 2 angles are cut by a transversal so the alternate interior angles are congruent, then the lines are parallel", "Converse Exterior Angles Theorem" : "If 2 lines are cut by a transversal so the alternate exterior angles are congruent, then the lines are parallel", "Converse of Consecutive Interior Angles Theorem" : "If 2 lines are cut by a transveral so the consecutive interior angles are supplementary, then the lines are parallel", "Perpendicular Transversal Theorem" : "If a transversal is perpendicular to 1 of 2 parallel lines, then it is perpendicular to the other", "Lines Perpendicular to a Transerval Theorem" : "In a plane, if 2 lines are perpendicular to the same line, then they are parallel to each other", "Triangle Sum Theorem" : "Sum of the measures of the interior angles of a triangle is 180°", "Exterior Angles Theorem" : "The measure of an exterior angle of a triangle is equal to the sum of the measures of the two nonadjacent interior angles", "Base Angles Theorem" : "If two sides of a triangle are congruent, then the angles opposite those sides are congruent. (Base angles of an isosceles triangle are congruent.)", "Converse of the Base Angles Theorem" : "If 2 angles of a triangle are congruent, the the sides opposite those angles are congruent"}       
ifthenstatements2=["If 2 lines intersect to form a linear pair of congruent angles","If 2 lines are perpendicular","If 2 sides of 2 adjacent acute angles are perpendicular"]
ifthenstatements={"If 2 lines intersect to form a linear pair of congruent angles" : "then the lines are perpendicular", "If 2 lines are perpendicular" : "then they intersect to form right angles", "If 2 sides of 2 adjacent acute angles are perpendicular" : "then the angles are complementary"}
corallaries2=["Corollary to the Triangle Sum Theorem","Corollary to the Base Angles Theorem","Corollary to the Base Angles Theorem","Corollary to the Converse of the Base Angles Theorem"]
corallaries={"Corollary to the Triangle Sum Theorem" : "Acute angles of a right triangle are complementary", "Corollary to the Base Angles Theorem" : "If a triangle is equilateral, then it is equiangular", "Corollary to the Base Angles Theorem" : "If a triangle is equilateral, then it is equiangular", "Corollary to the Converse of the Base Angles Theorem" : "If a triangle is equiangular, then it is equilateral"}

check=False
while check==False:
    study=input("What do you want to study? The options are : Point Line and Plane, Postulates, Shapes, Properties, Theorems, If Then Statements, and Corallaries")
    if study=="Point Line and Plane" or study=="Postulates" or study=="Shapes" or study=="Properties" or study=="Theorems" or study=="If Then Statements" or study=="Corallaries":
            check=True
    else:
        print("That is not a valid option. Please try again.")
        
dictionaries={"Point Line and Plane" : pointlineandplane, "Postulates" : postulates, "Shapes" : shapes, "Properties" : properties, "Theorems" : theorems, "If Then Statements" : ifthenstatements, "Corallaries" : corallaries}
topic=dictionaries[study]

if topic==pointlineandplane:
    topic2=pointlineandplane2
if topic==postulates:
    topic2=postulates2
if topic==shapes:
    topic2=shapes2
if topic==properties:
    topic2=properties2
if topic==theorems:
    topic2=theorems2
if topic==ifthenstatements:
    topic2=ifthenstatements2
if topic==corallaries:
    topic2=corallaries2
    
x=0
wrongs=[]

end=False
y=0
zx=0
g=True
zxy=0

while end!=True:
    for zx in range(0, len(topic2)):
        wrongs.append(0)
        answer=input("\nComplete the following statement \n\n" + topic2[zx])
        if answer==topic[topic2[zx]]:
            print("You got it right! Good job!")
        else:
            print("You got it wrong\nThe correct answer is '" + topic[topic2[zx]] + "'")
            wrongs.append(topic2[zx])
    print("\nBefore you go, please redo the ones you got wrong")           
    for sa in wrongs:
        if sa!=0:
            answers2=input("\nComplete the following statement \n" + topic[sa])
            if answers2==sa:
                print("You got it right!")
            else:
                print("You got it wrong. The correct answer is '" + sa +"'")
    end=True
                   
