#include<iostream>
#include<vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

const int SIZE = 13;
const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

int perceptionVariant;               
pair<int, int> gollum = {-1, -1};
pair<int, int> mountDoom = {-1, -1};
bool foundGollum = false;
bool foundMount = false;
int pathLen = 0;


bool inBounds(int x, int y); //Check if coordinates within the map
void markDanger(int x, int y, char type); //mark cell like dangerous
void readPerception(); // Reads the response from the interactor after the movement
void moveTo(int x, int y);
bool backtrack(int x, int y);


struct Cell{
    bool safe = true;
    bool visited = false;
    char type = ' ';
};

Cell grid[SIZE][SIZE];

int main(){

}
