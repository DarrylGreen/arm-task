from conveyor import Conveyor

def setup_conveyor_for_test(conveyor_item):
    test_conveyor = Conveyor(25)
    for i in range(25):
        test_conveyor.belt[i] = conveyor_item
    test_conveyor.top_workers[0].items = set()
    test_conveyor.bottom_workers[0].items = set()
    test_conveyor.top_workers[1].items = set()
    test_conveyor.bottom_workers[1].items = set(['A'])
    test_conveyor.top_workers[2].items = set()
    test_conveyor.bottom_workers[2].items = set(['B'])
    test_conveyor.top_workers[3].items = set()
    test_conveyor.bottom_workers[3].items = set(['A', 'B'])
    test_conveyor.top_workers[4].items = set()
    test_conveyor.bottom_workers[4].items = set(['F'])
    test_conveyor.top_workers[5].items = set(['A'])
    test_conveyor.bottom_workers[5].items = set()
    test_conveyor.top_workers[6].items = set(['A'])
    test_conveyor.bottom_workers[6].items = set(['A'])
    test_conveyor.top_workers[7].items = set(['A'])
    test_conveyor.bottom_workers[7].items = set(['B'])
    test_conveyor.top_workers[8].items = set(['A'])
    test_conveyor.bottom_workers[8].items = set(['A', 'B'])
    test_conveyor.top_workers[9].items = set(['A'])
    test_conveyor.bottom_workers[9].items = set(['F'])
    test_conveyor.top_workers[10].items = set(['B'])
    test_conveyor.bottom_workers[10].items = set()
    test_conveyor.top_workers[11].items = set(['B'])
    test_conveyor.bottom_workers[11].items = set(['A'])
    test_conveyor.top_workers[12].items = set(['B'])
    test_conveyor.bottom_workers[12].items = set(['B'])
    test_conveyor.top_workers[13].items = set(['B'])
    test_conveyor.bottom_workers[13].items = set(['A', 'B'])
    test_conveyor.top_workers[14].items = set(['B'])
    test_conveyor.bottom_workers[14].items = set(['F'])
    test_conveyor.top_workers[15].items = set(['A', 'B'])
    test_conveyor.bottom_workers[15].items = set()
    test_conveyor.top_workers[16].items = set(['A', 'B'])
    test_conveyor.bottom_workers[16].items = set(['A'])
    test_conveyor.top_workers[17].items = set(['A', 'B'])
    test_conveyor.bottom_workers[17].items = set(['B'])
    test_conveyor.top_workers[18].items = set(['A', 'B'])
    test_conveyor.bottom_workers[18].items = set(['A', 'B'])
    test_conveyor.top_workers[19].items = set(['A', 'B'])
    test_conveyor.bottom_workers[19].items = set(['F'])
    test_conveyor.top_workers[20].items = set(['F'])
    test_conveyor.bottom_workers[20].items = set()
    test_conveyor.top_workers[21].items = set(['F'])
    test_conveyor.bottom_workers[21].items = set(['A'])
    test_conveyor.top_workers[22].items = set(['F'])
    test_conveyor.bottom_workers[22].items = set(['B'])
    test_conveyor.top_workers[23].items = set(['F'])
    test_conveyor.bottom_workers[23].items = set(['A', 'B'])
    test_conveyor.top_workers[24].items = set(['F'])
    test_conveyor.bottom_workers[24].items = set(['F'])
    return test_conveyor


def test_end_of_belt():
    test_conveyor_A = Conveyor(1)
    test_conveyor_A.belt[1] = 'A'
    test_conveyor_A.check_end_of_belt()
    test_conveyor_B = Conveyor(1)
    test_conveyor_B.belt[1] = 'B'
    test_conveyor_B.check_end_of_belt()
    test_conveyor_F = Conveyor(1)
    test_conveyor_F.belt[1] = 'F'
    test_conveyor_F.check_end_of_belt()
    test_conveyor_space = Conveyor(1)
    test_conveyor_space.belt[1] = ' '
    test_conveyor_space.check_end_of_belt()
    assert test_conveyor_A.finished_items == 0
    assert test_conveyor_A.untouched_A_components == 1
    assert test_conveyor_A.untouched_B_components == 0
    assert test_conveyor_B.finished_items == 0
    assert test_conveyor_B.untouched_A_components == 0
    assert test_conveyor_B.untouched_B_components == 1
    assert test_conveyor_F.finished_items == 1
    assert test_conveyor_F.untouched_A_components == 0
    assert test_conveyor_F.untouched_B_components == 0
    assert test_conveyor_space.finished_items == 0
    assert test_conveyor_space.untouched_A_components == 0
    assert test_conveyor_space.untouched_B_components == 0


def test_component_A():
    test_conveyor = setup_conveyor_for_test('A')
    for i in range(25):
        test_conveyor.handle_belt_position(i)
    assert test_conveyor.belt[0] == ' '
    assert test_conveyor.belt[1] == ' '
    assert test_conveyor.belt[2] == ' '
    assert test_conveyor.belt[3] == ' '
    assert test_conveyor.belt[4] == ' '
    assert test_conveyor.belt[5] == ' '
    assert test_conveyor.belt[6] == 'A'
    assert test_conveyor.belt[7] == ' '
    assert test_conveyor.belt[8] == 'A'
    assert test_conveyor.belt[9] == 'A'
    assert test_conveyor.belt[10] == ' '
    assert test_conveyor.belt[11] == ' '
    assert test_conveyor.belt[12] == ' '
    assert test_conveyor.belt[13] == ' '
    assert test_conveyor.belt[14] == ' '
    assert test_conveyor.belt[15] == ' '
    assert test_conveyor.belt[16] == 'A'
    assert test_conveyor.belt[17] == ' '
    assert test_conveyor.belt[18] == 'A'
    assert test_conveyor.belt[19] == 'A'
    assert test_conveyor.belt[20] == ' '
    assert test_conveyor.belt[21] == 'A'
    assert test_conveyor.belt[22] == ' '
    assert test_conveyor.belt[23] == 'A'
    assert test_conveyor.belt[24] == 'A'
    assert test_conveyor.top_workers[0].items == set(['A'])
    assert test_conveyor.top_workers[1].items == set(['A'])
    assert test_conveyor.top_workers[2].items == set()
    assert test_conveyor.top_workers[3].items == set(['A'])
    assert test_conveyor.top_workers[4].items == set(['A'])
    assert test_conveyor.top_workers[5].items == set(['A'])
    assert test_conveyor.top_workers[6].items == set(['A'])
    assert test_conveyor.top_workers[7].items == set(['A'])
    assert test_conveyor.top_workers[8].items == set(['A'])
    assert test_conveyor.top_workers[9].items == set(['A'])
    assert test_conveyor.top_workers[10].items == set(['A', 'B'])
    assert test_conveyor.top_workers[11].items == set(['A', 'B'])
    assert test_conveyor.top_workers[12].items == set(['A', 'B'])
    assert test_conveyor.top_workers[13].items == set(['A', 'B'])
    assert test_conveyor.top_workers[14].items == set(['A', 'B'])
    assert test_conveyor.top_workers[15].items == set(['A', 'B'])
    assert test_conveyor.top_workers[16].items == set(['A', 'B'])
    assert test_conveyor.top_workers[17].items == set(['A', 'B'])
    assert test_conveyor.top_workers[18].items == set(['A', 'B'])
    assert test_conveyor.top_workers[19].items == set(['A', 'B'])
    assert test_conveyor.top_workers[20].items == set(['F'])
    assert test_conveyor.top_workers[21].items == set(['F'])
    assert test_conveyor.top_workers[22].items == set(['F'])
    assert test_conveyor.top_workers[23].items == set(['F'])
    assert test_conveyor.top_workers[24].items == set(['F'])
    assert test_conveyor.bottom_workers[0].items == set()
    assert test_conveyor.bottom_workers[1].items == set(['A'])
    assert test_conveyor.bottom_workers[2].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[3].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[4].items == set(['F'])
    assert test_conveyor.bottom_workers[5].items == set(['A'])
    assert test_conveyor.bottom_workers[6].items == set(['A'])
    assert test_conveyor.bottom_workers[7].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[8].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[9].items == set(['F'])
    assert test_conveyor.bottom_workers[10].items == set()
    assert test_conveyor.bottom_workers[11].items == set(['A'])
    assert test_conveyor.bottom_workers[12].items == set(['B'])
    assert test_conveyor.bottom_workers[13].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[14].items == set(['F'])
    assert test_conveyor.bottom_workers[15].items == set(['A'])
    assert test_conveyor.bottom_workers[16].items == set(['A'])
    assert test_conveyor.bottom_workers[17].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[18].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[19].items == set(['F'])
    assert test_conveyor.bottom_workers[20].items == set(['A'])
    assert test_conveyor.bottom_workers[21].items == set(['A'])
    assert test_conveyor.bottom_workers[22].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[23].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[24].items == set(['F'])
    

def test_component_B():
    test_conveyor = setup_conveyor_for_test('B')
    for i in range(25):
        test_conveyor.handle_belt_position(i)
    assert test_conveyor.belt[0] == ' '
    assert test_conveyor.belt[1] == ' '
    assert test_conveyor.belt[2] == ' '
    assert test_conveyor.belt[3] == ' '
    assert test_conveyor.belt[4] == ' '
    assert test_conveyor.belt[5] == ' '
    assert test_conveyor.belt[6] == ' '
    assert test_conveyor.belt[7] == ' '
    assert test_conveyor.belt[8] == ' '
    assert test_conveyor.belt[9] == ' '
    assert test_conveyor.belt[10] == ' '
    assert test_conveyor.belt[11] == ' '
    assert test_conveyor.belt[12] == 'B'
    assert test_conveyor.belt[13] == 'B'
    assert test_conveyor.belt[14] == 'B'
    assert test_conveyor.belt[15] == ' '
    assert test_conveyor.belt[16] == ' '
    assert test_conveyor.belt[17] == 'B'
    assert test_conveyor.belt[18] == 'B'
    assert test_conveyor.belt[19] == 'B'
    assert test_conveyor.belt[20] == ' '
    assert test_conveyor.belt[21] == ' '
    assert test_conveyor.belt[22] == 'B'
    assert test_conveyor.belt[23] == 'B'
    assert test_conveyor.belt[24] == 'B'
    assert test_conveyor.top_workers[0].items == set(['B'])
    assert test_conveyor.top_workers[1].items == set()
    assert test_conveyor.top_workers[2].items == set(['B'])
    assert test_conveyor.top_workers[3].items == set(['B'])
    assert test_conveyor.top_workers[4].items == set(['B'])
    assert test_conveyor.top_workers[5].items == set(['A', 'B'])
    assert test_conveyor.top_workers[6].items == set(['A', 'B'])
    assert test_conveyor.top_workers[7].items == set(['A', 'B'])
    assert test_conveyor.top_workers[8].items == set(['A', 'B'])
    assert test_conveyor.top_workers[9].items == set(['A', 'B'])
    assert test_conveyor.top_workers[10].items == set(['B'])
    assert test_conveyor.top_workers[11].items == set(['B'])
    assert test_conveyor.top_workers[12].items == set(['B'])
    assert test_conveyor.top_workers[13].items == set(['B'])
    assert test_conveyor.top_workers[14].items == set(['B'])
    assert test_conveyor.top_workers[15].items == set(['A', 'B'])
    assert test_conveyor.top_workers[16].items == set(['A', 'B'])
    assert test_conveyor.top_workers[17].items == set(['A', 'B'])
    assert test_conveyor.top_workers[18].items == set(['A', 'B'])
    assert test_conveyor.top_workers[19].items == set(['A', 'B'])
    assert test_conveyor.top_workers[20].items == set(['F'])
    assert test_conveyor.top_workers[21].items == set(['F'])
    assert test_conveyor.top_workers[22].items == set(['F'])
    assert test_conveyor.top_workers[23].items == set(['F'])
    assert test_conveyor.top_workers[24].items == set(['F'])
    assert test_conveyor.bottom_workers[0].items == set()
    assert test_conveyor.bottom_workers[1].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[2].items == set(['B'])
    assert test_conveyor.bottom_workers[3].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[4].items == set(['F'])
    assert test_conveyor.bottom_workers[5].items == set()
    assert test_conveyor.bottom_workers[6].items == set(['A'])
    assert test_conveyor.bottom_workers[7].items == set(['B'])
    assert test_conveyor.bottom_workers[8].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[9].items == set(['F'])
    assert test_conveyor.bottom_workers[10].items == set(['B'])
    assert test_conveyor.bottom_workers[11].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[12].items == set(['B'])
    assert test_conveyor.bottom_workers[13].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[14].items == set(['F'])
    assert test_conveyor.bottom_workers[15].items == set(['B'])
    assert test_conveyor.bottom_workers[16].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[17].items == set(['B'])
    assert test_conveyor.bottom_workers[18].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[19].items == set(['F'])
    assert test_conveyor.bottom_workers[20].items == set(['B'])
    assert test_conveyor.bottom_workers[21].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[22].items == set(['B'])
    assert test_conveyor.bottom_workers[23].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[24].items == set(['F'])


def test_empty_space():
    test_conveyor = setup_conveyor_for_test(' ')
    for i in range(25):
        test_conveyor.handle_belt_position(i)
    assert test_conveyor.belt[0] == ' '
    assert test_conveyor.belt[1] == ' '
    assert test_conveyor.belt[2] == ' '
    assert test_conveyor.belt[3] == ' '
    assert test_conveyor.belt[4] == 'F'
    assert test_conveyor.belt[5] == ' '
    assert test_conveyor.belt[6] == ' '
    assert test_conveyor.belt[7] == ' '
    assert test_conveyor.belt[8] == ' '
    assert test_conveyor.belt[9] == 'F'
    assert test_conveyor.belt[10] == ' '
    assert test_conveyor.belt[11] == ' '
    assert test_conveyor.belt[12] == ' '
    assert test_conveyor.belt[13] == ' '
    assert test_conveyor.belt[14] == 'F'
    assert test_conveyor.belt[15] == ' '
    assert test_conveyor.belt[16] == ' '
    assert test_conveyor.belt[17] == ' '
    assert test_conveyor.belt[18] == ' '
    assert test_conveyor.belt[19] == 'F'
    assert test_conveyor.belt[20] == 'F'
    assert test_conveyor.belt[21] == 'F'
    assert test_conveyor.belt[22] == 'F'
    assert test_conveyor.belt[23] == 'F'
    assert test_conveyor.belt[24] == 'F'
    assert test_conveyor.top_workers[0].items == set()
    assert test_conveyor.top_workers[1].items == set()
    assert test_conveyor.top_workers[2].items == set()
    assert test_conveyor.top_workers[3].items == set()
    assert test_conveyor.top_workers[4].items == set()
    assert test_conveyor.top_workers[5].items == set(['A'])
    assert test_conveyor.top_workers[6].items == set(['A'])
    assert test_conveyor.top_workers[7].items == set(['A'])
    assert test_conveyor.top_workers[8].items == set(['A'])
    assert test_conveyor.top_workers[9].items == set(['A'])
    assert test_conveyor.top_workers[10].items == set(['B'])
    assert test_conveyor.top_workers[11].items == set(['B'])
    assert test_conveyor.top_workers[12].items == set(['B'])
    assert test_conveyor.top_workers[13].items == set(['B'])
    assert test_conveyor.top_workers[14].items == set(['B'])
    assert test_conveyor.top_workers[15].items == set(['A', 'B'])
    assert test_conveyor.top_workers[16].items == set(['A', 'B'])
    assert test_conveyor.top_workers[17].items == set(['A', 'B'])
    assert test_conveyor.top_workers[18].items == set(['A', 'B'])
    assert test_conveyor.top_workers[19].items == set(['A', 'B'])
    assert test_conveyor.top_workers[20].items == set()
    assert test_conveyor.top_workers[21].items == set()
    assert test_conveyor.top_workers[22].items == set()
    assert test_conveyor.top_workers[23].items == set()
    assert test_conveyor.top_workers[24].items == set()
    assert test_conveyor.bottom_workers[0].items == set()
    assert test_conveyor.bottom_workers[1].items == set(['A'])
    assert test_conveyor.bottom_workers[2].items == set(['B'])
    assert test_conveyor.bottom_workers[3].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[4].items == set()
    assert test_conveyor.bottom_workers[5].items == set()
    assert test_conveyor.bottom_workers[6].items == set(['A'])
    assert test_conveyor.bottom_workers[7].items == set(['B'])
    assert test_conveyor.bottom_workers[8].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[9].items == set()
    assert test_conveyor.bottom_workers[10].items == set()
    assert test_conveyor.bottom_workers[11].items == set(['A'])
    assert test_conveyor.bottom_workers[12].items == set(['B'])
    assert test_conveyor.bottom_workers[13].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[14].items == set()
    assert test_conveyor.bottom_workers[15].items == set()
    assert test_conveyor.bottom_workers[16].items == set(['A'])
    assert test_conveyor.bottom_workers[17].items == set(['B'])
    assert test_conveyor.bottom_workers[18].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[19].items == set()
    assert test_conveyor.bottom_workers[20].items == set()
    assert test_conveyor.bottom_workers[21].items == set(['A'])
    assert test_conveyor.bottom_workers[22].items == set(['B'])
    assert test_conveyor.bottom_workers[23].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[24].items == set(['F'])


def test_finished_product():
    test_conveyor = setup_conveyor_for_test('F')
    for i in range(25):
        test_conveyor.handle_belt_position(i)
    assert test_conveyor.belt[0] == 'F'
    assert test_conveyor.belt[1] == 'F'
    assert test_conveyor.belt[2] == 'F'
    assert test_conveyor.belt[3] == 'F'
    assert test_conveyor.belt[4] == 'F'
    assert test_conveyor.belt[5] == 'F'
    assert test_conveyor.belt[6] == 'F'
    assert test_conveyor.belt[7] == 'F'
    assert test_conveyor.belt[8] == 'F'
    assert test_conveyor.belt[9] == 'F'
    assert test_conveyor.belt[10] == 'F'
    assert test_conveyor.belt[11] == 'F'
    assert test_conveyor.belt[12] == 'F'
    assert test_conveyor.belt[13] == 'F'
    assert test_conveyor.belt[14] == 'F'
    assert test_conveyor.belt[15] == 'F'
    assert test_conveyor.belt[16] == 'F'
    assert test_conveyor.belt[17] == 'F'
    assert test_conveyor.belt[18] == 'F'
    assert test_conveyor.belt[19] == 'F'
    assert test_conveyor.belt[20] == 'F'
    assert test_conveyor.belt[21] == 'F'
    assert test_conveyor.belt[22] == 'F'
    assert test_conveyor.belt[23] == 'F'
    assert test_conveyor.belt[24] == 'F'
    assert test_conveyor.top_workers[0].items == set([])
    assert test_conveyor.top_workers[1].items == set([])
    assert test_conveyor.top_workers[2].items == set([])
    assert test_conveyor.top_workers[3].items == set([])
    assert test_conveyor.top_workers[4].items == set([])
    assert test_conveyor.top_workers[5].items == set(['A'])
    assert test_conveyor.top_workers[6].items == set(['A'])
    assert test_conveyor.top_workers[7].items == set(['A'])
    assert test_conveyor.top_workers[8].items == set(['A'])
    assert test_conveyor.top_workers[9].items == set(['A'])
    assert test_conveyor.top_workers[10].items == set(['B'])
    assert test_conveyor.top_workers[11].items == set(['B'])
    assert test_conveyor.top_workers[12].items == set(['B'])
    assert test_conveyor.top_workers[13].items == set(['B'])
    assert test_conveyor.top_workers[14].items == set(['B'])
    assert test_conveyor.top_workers[15].items == set(['A', 'B'])
    assert test_conveyor.top_workers[16].items == set(['A', 'B'])
    assert test_conveyor.top_workers[17].items == set(['A', 'B'])
    assert test_conveyor.top_workers[18].items == set(['A', 'B'])
    assert test_conveyor.top_workers[19].items == set(['A', 'B'])
    assert test_conveyor.top_workers[20].items == set(['F'])
    assert test_conveyor.top_workers[21].items == set(['F'])
    assert test_conveyor.top_workers[22].items == set(['F'])
    assert test_conveyor.top_workers[23].items == set(['F'])
    assert test_conveyor.top_workers[24].items == set(['F'])
    assert test_conveyor.bottom_workers[0].items == set([])
    assert test_conveyor.bottom_workers[1].items == set(['A'])
    assert test_conveyor.bottom_workers[2].items == set(['B'])
    assert test_conveyor.bottom_workers[3].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[4].items == set(['F'])
    assert test_conveyor.bottom_workers[5].items == set([])
    assert test_conveyor.bottom_workers[6].items == set(['A'])
    assert test_conveyor.bottom_workers[7].items == set(['B'])
    assert test_conveyor.bottom_workers[8].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[9].items == set(['F'])
    assert test_conveyor.bottom_workers[10].items == set([])
    assert test_conveyor.bottom_workers[11].items == set(['A'])
    assert test_conveyor.bottom_workers[12].items == set(['B'])
    assert test_conveyor.bottom_workers[13].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[14].items == set(['F'])
    assert test_conveyor.bottom_workers[15].items == set([])
    assert test_conveyor.bottom_workers[16].items == set(['A'])
    assert test_conveyor.bottom_workers[17].items == set(['B'])
    assert test_conveyor.bottom_workers[18].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[19].items == set(['F'])
    assert test_conveyor.bottom_workers[20].items == set([])
    assert test_conveyor.bottom_workers[21].items == set(['A'])
    assert test_conveyor.bottom_workers[22].items == set(['B'])
    assert test_conveyor.bottom_workers[23].items == set(['A', 'B'])
    assert test_conveyor.bottom_workers[24].items == set(['F'])
