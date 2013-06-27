ArrayList<Point> randomPoints;
BasePoint base;


void setup() {
  size(1200,800);
  randomPoints = new ArrayList<Point>();  // Create an empty ArrayList
  base = new BasePoint(random(width), random(height), 100);
  for(int i = 0; i < 100; i++){
    randomPoints.add(new Point(random(width), random(height)));  // Start by adding one element
  }
}

void draw() {
  background(255);
  fill(0);
  text("Move Your Mouse highlight points withn Radius. Click to Move Base Point.", 20,20);
  // Display Random Points
  for (int i = randomPoints.size()-1; i >= 0; i--) {
    Point currentPoint = randomPoints.get(i);
    currentPoint.display();
  }
  // Display Base Point
  base.display();
  // Find Points within Circle
  for (int i = randomPoints.size()-1; i >= 0; i--) {
    Point currentPoint = randomPoints.get(i);
    float distance = dist(currentPoint.x, currentPoint.y, base.x,base.y);
    if(distance < base.r){
      // Draw a Circle Around it
      ellipseMode(RADIUS);
      stroke(255,0,0);
      noFill();
      ellipse(currentPoint.x,currentPoint.y,15,15);
    }
  }
}

void mouseMoved(){
  base.r = dist(base.x, base.y, mouseX, mouseY);
}

void mousePressed(){
  base.x = mouseX;
  base.y = mouseY;
}

class Point { 
  float x;
  float y;
  float distance;

  // The Constructor is defined with arguments.
  Point(float tempX, float tempY) { 
    x = tempX;
    y = tempY;
  }

  void display() {
    noStroke();
    fill(0);
    ellipseMode(CENTER);
    ellipse(x,y,5,5);
  }
}

class BasePoint { 
  float x;
  float y;
  float r;
  float distance;

  // The Constructor is defined with arguments.
  BasePoint(float tempX, float tempY, float tempR) { 
    x = tempX;
    y = tempY;
    r = tempR;
  }

  void display() {
    // Draw Point
    noStroke();
    fill(255,0,0);
    ellipseMode(CENTER);
    ellipse(x,y,5,5);
    // Draw Outside Ring
    ellipseMode(RADIUS);
    stroke(255,0,0);
    noFill();
    ellipse(x,y,r,r);
  }
}

