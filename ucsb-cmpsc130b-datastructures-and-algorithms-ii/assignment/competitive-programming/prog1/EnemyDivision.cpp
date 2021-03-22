/*
https://open.kattis.com/problems/enemydivision
*/

#include <iostream>
#include <vector>

int main()
{
    int n, m; std::cin >> n >> m;
    std::vector<std::vector<int>> map(n);

    for(int i=0; i<m; ++i)
    {
        int a, b; std::cin >> a >> b;
        a--; b--;
        map[a].push_back(b); map[b].push_back(a);
    }

    // use (0,1,2) to classify each person; 2 is the initial status
    std::vector<int> group(n, 2), enemy(n, 0);
    for(int i=0; i<n; ++i)
    {
        // add the enemy of current person to group number
        std::vector<int> count_group(3);
        for(int l=0; l < map[i].size(); ++l) {
            int group_l = group[map[i][l]]; count_group[group_l]++;
        }  

        int current = i, flag = 0;
        // if the group 0 has more than one enemy, then assign it to group 1
        if (count_group[0] >=2 ) {
            flag = 1;
        }

        while (true)
        {
            int cur_enemy = -1;
            group[current] = flag;
            // for each enemy in the same group, record the number of enemey
            for(int j=0; j < map[i].size(); ++j) {
                int enemy_j = map[current][j];
                if (group[enemy_j] == flag) {
                    enemy[current]++; enemy[enemy_j]++;
                    // if one enemy has more than 2 enemy
                    if (enemy[enemy_j] == 2)
                    {
                        cur_enemy = enemy_j;
                        // if enemy's enemy in the same group
                        for (int k=0; k < map[cur_enemy].size(); ++k) {
                            int enemy_k = map[cur_enemy][k];
                            if (group[enemy_k] == flag)
                            {
                                enemy[enemy_k]--; enemy[cur_enemy]--;
                            }
                        }
                            
                    }
                }
            }
            // there does not exist enemy who has more than 2 enemies
            if (cur_enemy == -1) {
                break;
            }
            // let the current person be this enemy who has more than 2 enemies
            current = cur_enemy; flag = 1 - flag;
        }
    }

   std::vector<std::vector<int>> output(2);
    for (int i=0; i<n; ++i){
        output[group[i]].push_back(i);
    }
    // print number of groups
    if (output[1].empty()) {
        printf("1\n");
    } else {
        printf("2\n");
    }
    // for each group g
    for (int g=0; g<output.size(); ++g) {
        std::vector<int> group=output[g];
        // print members in this group
        if (!group.empty()) {
            for (int m=0; m<group.size(); ++m) {
                if (m != group.size()-1) {
                    std::cout << group[m]+1 << " ";
                } else {
                    std::cout << group[m]+1 << "\n";
                }
            }
        }
    }
}
