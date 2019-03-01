import processing.net.*;
Server server;
int port = 5000;


void setup() {
  fullScreen();
  server = new Server(this, port);
  background(#ffffff);
}

void draw() {
  background(#ffffff);
  Client client = server.available();
  if (client ==null) return;

  String[] gazeDataStrings = split(client.readString(), "\n");

  if (gazeDataStrings.length < 2)return;

  String lastGazeDataString = gazeDataStrings[gazeDataStrings.length-2];
  println(lastGazeDataString);
  float[]gazePos = float(split(lastGazeDataString, ","));

  stroke(#000000);
  fill(#000000);
  ellipse(gazePos[0], gazePos[1], 30, 30);
}
