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

bool hasRing = true;
bool ringOn = false;
bool hasCoat = false;

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
void putRingOn();
void removeRing();
bool backtrack(int x, int y);

struct Cell{
    bool safe = true;
    bool visited = false;
    char type = ' ';
};

Cell grid[SIZE][SIZE];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    
    cin >> perceptionVariant;
    cin >> gollum.first >> gollum.second;

    readPerception();

    backtrack(0, 0);

    if (!foundMount) {
        cout << "e -1" << endl;
        cout.flush();
    }

    return 0;
}


bool inBounds(int x, int y){
    return x >= 0 && x < SIZE && y >= 0 && y < SIZE;
}

void markDanger(int x, int y, char type){
    if (inBounds(x, y) == false) return;

    int radius = 0;
    bool moore = false;

        if (type == 'O') { // Orc Patrol
        radius = (hasCoat || ringOn) ? 0 : 1;
        moore = false;
    }
    else if (type == 'U') { // Uruk-hai
        radius = (hasCoat || ringOn) ? 1 : 2;
        moore = false;
    }
    else if (type == 'N') { // Nazgûl
        if (ringOn) radius = 2; else radius = 1;
        moore = true;
    }
    else if (type == 'W') { // Watchtower
        radius = 2;
        moore = true;
    }

    grid[x][y].safe = false;
    grid[x][y].type = type;

    //  (Von Neumann)
    if (!moore) {
        for (int i = 1; i <= radius; i++) {

            // down
            if (inBounds(x + i, y)) {
                grid[x + i][y].safe = false;
                grid[x + i][y].type = type;
            }

            // up
            if (inBounds(x - i, y)) {
                grid[x - i][y].safe = false;
                grid[x - i][y].type = type;
            }

            // right
            if (inBounds(x, y + i)) {
                grid[x][y + i].safe = false;
                grid[x][y + i].type = type;
            }

            // left
            if (inBounds(x, y - i)) {
                grid[x][y - i].safe = false;
                grid[x][y - i].type = type;
            }
        }
    }

    else {
        for (int i = -radius; i <= radius; i++) {
            for (int j = -radius; j <= radius; j++) {
                int nx = x + i, ny = y + j;
                if (inBounds(nx, ny)) {
                    grid[nx][ny].safe = false;
                    grid[nx][ny].type = type;
                }
            }
        }
    }
}



void readPerception(){
    int n;
    if (!(cin >> n)) exit(0); 

    for (int i = 0; i < n; i++) {
        int x, y; char t;
        cin >> x >> y >> t;

        if (t == 'O' || t == 'U' || t == 'N' || t == 'W')
            markDanger(x, y, t);

        if (t == 'P')
            if (inBounds(x, y)) grid[x][y].safe = false;

        // Gollum
        if (t == 'G') {
            gollum = {x, y};
        }

        // Mount Doom
        if (t == 'M') {
            mountDoom = {x, y};
        }

        // Mithril Coat
        if (t == 'C') {
            hasCoat = true;
        }
    }
}

void moveTo(int x, int y) {
    cout << "m " << x << " " << y << endl;
    cout.flush();
    readPerception();

    if (cin.peek() == 'M') {
        string tmp;
        cin >> tmp >> tmp >> tmp >> tmp >> mountDoom.first >> mountDoom.second;
        foundGollum = true;
    }
}

void putRingOn() {
    if (!ringOn) {
        cout << "r" << endl;
        cout.flush();
        ringOn = true;
        readPerception();
    }
}


void removeRing() {
    if (ringOn) {
        cout << "rr" << endl;
        cout.flush();
        ringOn = false;
        readPerception();
    }
}

bool backtrack(int x, int y) {
    if(foundMount && x == mountDoom.first && y == mountDoom.second) {
        cout << "e " << pathLen << endl; 
        cout.flush();
        return true;
    }

    grid[x][y].visited = true;

    for( int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(inBounds(nx, ny) && !grid[nx][ny].visited && grid[nx][ny].safe){
            moveTo(nx, ny);
            pathLen++;

            if (foundGollum && !foundMount && mountDoom.first != -1){
                foundMount = true;
            }
            if(backtrack(nx, ny)){
                return true;
            }
            else{
                moveTo(x, y);
                pathLen--;
            }
        }
    }
    return false;
}