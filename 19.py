import copy

import numpy as np
input = """--- scanner 0 ---
752,-783,692
474,747,497
-397,-300,-598
-469,945,901
615,-711,762
32,-3,30
342,-636,-714
869,819,-420
-541,813,-817
-391,943,801
-385,857,-786
-738,-525,468
-624,-395,466
311,-645,-467
827,935,-521
-73,182,84
-499,-355,-616
-444,662,-796
767,-731,783
-467,-303,-666
854,711,-494
343,-586,-598
395,716,532
-620,-568,440
-514,921,826
514,563,511

--- scanner 1 ---
-858,-911,-411
-933,420,-237
387,-588,-465
-167,14,55
-738,497,571
435,-457,-407
559,297,855
673,-679,434
432,724,-528
444,-587,-552
-64,-163,116
-504,-865,898
-876,350,-372
-655,-818,839
-793,-870,-533
-657,655,623
530,682,-676
342,711,-710
531,225,838
-693,-908,-451
-507,-902,868
503,251,722
-628,415,621
671,-701,503
-979,418,-272
533,-604,508

--- scanner 2 ---
812,490,-557
737,519,337
-511,407,-339
435,-496,-650
-547,-602,539
911,-780,342
759,581,445
-629,440,-412
-456,720,506
746,596,546
422,-330,-593
443,-335,-607
-421,-382,-753
847,600,-615
-557,-523,474
944,484,-659
937,-767,485
-445,789,400
-489,-504,-737
-542,-759,461
949,-693,392
-559,381,-450
-485,666,463
103,-4,-51
-415,-468,-689

--- scanner 3 ---
659,-445,690
852,355,437
836,333,618
-801,-706,422
727,-543,636
837,-673,-596
-830,-831,-502
-845,-800,-455
493,584,-474
-701,-804,-381
-772,-698,604
812,222,517
674,-434,625
584,570,-296
-72,-32,-45
-831,498,703
-855,491,-685
-725,403,671
714,-679,-502
43,-128,112
-648,449,-648
-843,434,820
494,638,-323
833,-778,-481
-831,-612,577
-604,487,-696

--- scanner 4 ---
534,494,-677
272,795,854
-687,-621,-540
-901,471,888
-1,-100,54
-552,467,-288
656,650,-671
-458,-586,688
-807,368,942
416,-925,-463
-459,-682,606
217,825,889
276,-588,417
-546,301,-225
414,-786,-504
373,731,936
-798,454,815
244,-591,525
635,478,-679
-469,-659,752
-175,52,112
-571,518,-265
282,-868,-471
-692,-464,-618
368,-601,487
-677,-700,-605

--- scanner 5 ---
719,755,453
364,425,-505
-562,-897,410
347,-527,-792
347,-692,704
376,-672,-896
-672,419,770
35,34,-102
-140,-30,17
704,807,544
268,-647,-818
438,281,-509
-786,549,768
-594,295,-697
485,296,-478
-608,-468,-831
426,-723,739
-439,-919,435
-595,-433,-847
-668,592,796
466,-539,725
-517,-505,-764
-517,-921,335
-439,325,-603
-621,354,-611
567,735,474

--- scanner 6 ---
-655,444,-449
849,-884,-546
-757,457,-491
510,490,-410
-626,-580,760
-730,491,-287
-504,246,888
156,4,-71
-338,-619,-591
517,522,-385
768,-813,-487
643,436,867
-746,-549,851
540,-866,469
819,508,819
-591,-583,845
-10,-112,35
-582,307,808
634,613,-389
381,-922,540
-646,210,770
910,-919,-495
-433,-659,-497
776,487,790
-280,-708,-498
364,-900,407

--- scanner 7 ---
769,530,-865
628,894,605
858,-335,-826
-499,931,-567
625,-360,366
-912,-659,-582
-939,-572,-471
-633,398,648
-583,434,517
-364,929,-667
-918,-459,-615
-109,95,-27
623,824,517
50,177,-152
511,-290,363
741,614,-948
-847,-466,550
-784,-475,396
-540,405,539
803,-362,-880
-820,-444,345
732,-342,-985
-417,884,-633
613,917,685
562,-349,265
685,559,-808

--- scanner 8 ---
-402,-487,-794
-602,893,428
-337,-538,587
485,-551,807
-736,680,-422
819,512,-355
936,-720,-459
-308,-720,579
-702,881,314
-575,-491,-820
938,-642,-359
-624,664,-521
-532,-373,-792
522,-642,740
-792,668,-648
-688,882,406
-278,-565,673
884,587,-370
793,849,661
797,965,558
758,501,-366
450,-564,823
859,769,518
914,-597,-434
66,152,-15

--- scanner 9 ---
284,-910,-622
-620,348,-467
-696,-681,-469
-930,235,759
344,-774,796
-660,410,-271
-671,-864,608
366,367,830
-965,281,757
-696,-634,-473
-784,-852,627
432,-897,731
-58,-9,67
-830,338,827
264,449,-735
-763,414,-387
398,559,762
269,-907,-548
268,323,-649
257,-833,780
-771,-915,493
-136,-148,-22
253,388,-724
309,-941,-571
-816,-641,-358
413,388,672

--- scanner 10 ---
559,-614,311
-649,541,-608
-392,-927,-476
-479,-965,-526
443,-662,313
730,-779,-852
-413,526,-595
352,672,-988
331,447,509
518,666,-925
-570,531,-673
-704,399,555
-668,473,603
-790,405,619
-837,-459,473
109,-68,-168
-405,-953,-619
606,-645,385
-842,-438,459
-676,-451,516
-18,-2,-26
392,387,401
438,297,499
569,647,-948
733,-853,-807
820,-870,-944

--- scanner 11 ---
419,529,-486
-341,-704,629
757,-689,-847
-439,-660,-850
857,-792,-779
122,86,-128
435,868,334
-709,442,-420
-393,916,536
-337,-578,715
-619,972,548
-6,176,13
-471,-468,-782
-486,-639,-692
892,-746,-777
453,717,-515
457,782,323
343,882,335
601,619,-473
-581,416,-532
690,-613,367
587,-617,251
547,-679,447
-686,494,-580
-492,804,552
-326,-639,704

--- scanner 12 ---
552,-766,780
-630,-515,-528
90,0,-68
681,-707,-660
-446,506,-773
-35,-147,43
-504,427,-650
791,318,610
677,316,740
-655,-532,-560
-404,465,-712
413,628,-874
-642,-611,-436
-699,542,352
-714,633,404
845,-726,-549
460,544,-779
-258,-617,490
-562,612,424
673,290,567
484,486,-856
520,-816,832
-290,-748,549
450,-748,835
-289,-864,499
809,-650,-678

--- scanner 13 ---
-755,791,-670
-96,118,-153
605,-601,333
-628,-628,-932
462,-681,399
-857,775,-714
383,810,670
316,719,707
386,451,-562
-657,-807,-872
529,-595,-649
300,732,742
-772,720,-737
-525,-492,535
17,-14,-1
-547,-456,576
565,-797,395
529,-599,-696
-533,473,367
-735,-738,-916
-524,-348,672
-610,420,363
405,585,-656
-703,424,306
406,410,-612
409,-710,-656

--- scanner 14 ---
345,350,716
693,-671,890
-737,667,927
743,722,-443
408,-691,-386
-401,-383,579
-655,571,928
-486,-709,-213
413,492,698
-500,382,-509
554,-673,833
-493,-868,-339
-48,27,62
-441,480,-560
480,404,654
766,802,-458
673,634,-448
622,-679,907
-455,-486,485
-591,644,917
379,-748,-302
463,-831,-330
-528,-469,588
-511,483,-446
-513,-763,-268

--- scanner 15 ---
-849,806,-493
430,-651,-799
372,396,693
-420,640,805
-168,-67,141
484,-784,478
706,628,-854
698,532,-691
607,-660,457
502,-475,-751
-408,606,814
-925,-384,563
481,-518,-722
-694,835,-441
-776,693,-449
471,282,670
-71,58,33
-872,-754,-401
-890,-445,614
-412,545,804
-906,-930,-339
-819,-526,555
-928,-913,-472
787,495,-821
516,-777,453
378,292,513

--- scanner 16 ---
-574,-500,-845
-476,-648,-887
814,-765,748
749,-643,707
611,424,-578
782,439,-668
804,611,335
20,-25,12
-655,561,410
-650,455,401
-431,-711,425
128,-102,-170
818,774,445
-386,-466,-874
-351,639,-780
-702,566,527
762,694,505
649,-725,745
-488,-624,424
832,-804,-513
-479,-769,294
-273,534,-828
935,-904,-581
-299,662,-940
803,392,-510
889,-939,-583

--- scanner 17 ---
-566,-536,-428
496,-393,481
429,-317,-733
-523,799,-686
294,-260,-663
-514,-455,-586
639,-327,561
-490,-666,814
-623,878,355
488,936,-399
588,885,-514
599,-389,365
-513,-570,706
-564,-565,-668
475,873,-533
563,655,567
-594,938,534
-486,930,-611
-501,873,-531
563,702,563
-701,922,424
329,-214,-665
-491,-529,670
443,662,452
-96,161,65

--- scanner 18 ---
573,-571,-372
-6,-162,116
513,-515,-292
-651,381,848
-541,734,-608
-658,392,904
687,543,-443
574,577,-527
48,-32,-23
-476,611,-696
355,-389,696
489,518,-395
-644,-619,442
-442,-530,-674
448,-413,637
403,-529,-455
459,-565,704
-679,-491,444
-703,-560,419
518,369,570
-592,385,893
-600,-551,-627
513,338,791
-510,-722,-642
503,281,691
-492,670,-783

--- scanner 19 ---
-19,9,91
636,361,-519
627,479,383
-675,356,339
692,391,506
-883,-812,-785
617,-471,-462
628,252,-365
541,-396,-536
-789,675,-751
-726,331,370
-823,694,-692
-652,316,373
-462,-769,639
-783,-739,-743
-892,-721,-814
676,304,447
-577,-649,646
504,-624,416
-573,-649,599
731,397,-376
8,-112,-93
-828,617,-642
389,-724,365
523,-737,428
532,-392,-444

--- scanner 20 ---
-503,-916,-662
-639,551,-765
386,-831,812
-675,592,-743
642,-908,-770
-319,-740,444
717,-777,-733
562,-851,-755
837,275,541
699,587,-692
-420,-585,450
830,293,508
647,292,507
-479,478,559
-324,-856,-633
353,-917,835
-517,-687,458
-783,688,-766
617,477,-742
459,558,-690
-393,-900,-555
22,-61,51
531,-831,848
-370,431,423
-369,458,470

--- scanner 21 ---
-822,435,763
-31,110,95
-729,-786,941
98,-33,26
858,-792,855
-833,446,824
688,-678,-357
425,902,588
482,760,520
670,-780,-302
-394,-553,-397
738,-710,-305
-540,602,-787
428,782,472
-396,-439,-527
-766,614,-731
868,-733,660
-829,-708,943
845,669,-282
889,-636,811
-368,-557,-570
810,595,-298
-754,-663,919
-667,598,-619
-818,521,889
810,721,-385

--- scanner 22 ---
881,615,-673
-801,756,-546
114,-19,-77
810,-430,-609
758,709,-667
-378,-839,-699
702,-397,-506
-578,-357,352
594,-442,-596
-347,627,437
789,785,584
-388,-835,-638
465,-289,657
-387,-827,-733
590,-266,578
877,730,-568
-629,-322,291
-786,709,-515
-637,-428,433
444,-299,585
-38,108,-22
850,743,543
727,685,622
-275,490,507
-657,830,-542
-327,475,416

--- scanner 23 ---
-348,-769,-669
422,-588,382
-508,-566,807
-392,-522,904
427,-574,403
600,552,880
560,-492,-455
-289,-731,-599
-315,-842,-551
59,86,80
769,657,-623
4,-36,-73
-772,553,-441
659,520,768
-674,682,-429
-398,-624,772
474,-428,-461
816,610,-713
-605,896,379
-455,885,340
596,-444,-529
-461,908,406
517,461,861
-798,709,-538
588,-531,395
913,635,-563

--- scanner 24 ---
35,11,22
-868,-383,683
540,278,-744
-421,672,-425
472,-532,-461
342,-509,504
-651,-423,658
352,-450,699
424,277,-794
-698,730,328
-99,-77,-106
644,789,553
671,246,-803
718,804,661
617,762,777
321,-606,655
-475,699,-370
-400,-427,-859
-487,-564,-842
-316,692,-496
540,-462,-458
-702,-446,677
-490,-519,-768
-801,784,422
-715,657,431
522,-564,-513

--- scanner 25 ---
665,323,-848
-587,-871,816
746,-566,407
642,363,-882
-822,617,-344
591,338,-851
-574,-855,781
-440,-766,-582
-665,311,328
-620,386,352
855,-762,-582
128,-71,3
-265,-765,-538
-665,-788,744
-306,-785,-488
0,27,-92
-645,613,-349
942,-606,469
744,-642,-622
489,307,447
826,-709,473
-743,684,-392
740,-642,-575
564,322,382
478,318,508
-743,411,330

--- scanner 26 ---
524,319,504
838,-873,581
-762,604,-472
795,-893,-477
699,-816,579
670,450,-788
-236,-801,-650
719,449,-635
163,-156,146
-341,230,543
759,543,-730
829,-899,-322
-310,-468,766
-278,-917,-549
553,403,561
85,-21,52
-251,-693,-576
798,-808,-442
-368,285,489
767,-890,573
-256,-562,869
608,347,421
-348,356,384
-763,654,-356
-794,663,-603
-383,-571,783

--- scanner 27 ---
-457,-871,628
-349,772,655
885,795,-607
352,545,680
-608,-850,725
81,-64,52
-680,-407,-910
-748,-464,-768
584,-697,548
395,474,778
-5,35,-107
670,-692,-538
347,541,857
695,-751,636
-325,847,700
-796,-410,-790
-444,851,-454
598,-785,572
563,-663,-591
-327,747,778
-379,836,-529
851,835,-630
854,820,-556
784,-732,-589
-505,840,-443
-413,-840,784

--- scanner 28 ---
-332,-519,-394
-372,-386,-474
389,-496,-486
628,-575,850
712,701,-456
-510,270,-582
-600,-734,339
-457,379,-593
459,-550,-565
85,-122,39
636,592,332
-690,-802,366
475,-397,-490
533,670,439
-525,281,-647
-347,509,639
549,-576,746
640,-480,702
712,508,-496
-348,-497,-575
579,728,335
807,648,-451
-351,614,524
-47,-13,-68
-470,515,545
-691,-748,517

--- scanner 29 ---
-792,464,339
786,-494,353
404,461,368
-633,683,-863
-631,-756,422
-713,-794,522
-736,-339,-655
-157,-7,-6
-927,-372,-726
382,495,-773
-873,-310,-738
436,529,560
-892,532,236
-927,534,282
-746,664,-851
683,-470,-680
451,619,389
-733,798,-914
623,-384,367
551,-555,-739
706,-554,409
295,511,-832
-753,-797,357
470,560,-896
-23,87,-100
635,-668,-705

--- scanner 30 ---
508,-792,345
-454,656,-867
-746,728,376
-888,-443,-888
513,-714,502
-971,-768,337
-632,658,379
299,714,-590
-50,-66,-168
648,-462,-586
402,641,-573
-871,-580,-801
-399,683,-813
-525,676,-972
741,432,563
393,768,-487
523,-779,581
654,-399,-420
-983,-861,411
-695,669,278
-945,-911,324
731,578,540
-797,-535,-798
-188,-164,15
742,514,467
629,-439,-637

--- scanner 31 ---
435,559,529
889,430,-454
-845,-487,655
-630,-650,-820
845,-447,-548
816,-629,-556
-762,443,635
-615,-715,-809
133,-154,108
875,-602,-642
-863,-416,513
621,-794,823
-639,501,714
-789,456,-476
874,477,-423
-683,-661,-711
751,-680,825
-35,-94,27
578,-676,851
-670,477,-575
-701,401,676
415,711,508
-793,571,-581
745,356,-450
-768,-463,597
363,696,599

--- scanner 32 ---
805,-606,836
615,384,358
-440,-896,554
-492,-867,399
-416,-797,-846
556,465,429
918,539,-489
815,-667,840
-428,720,-727
-471,852,320
866,448,-474
806,-701,828
846,469,-626
-581,699,-846
5,-16,-70
136,-112,31
-561,-901,-817
536,-510,-829
-536,-823,-925
-338,869,342
-400,693,376
392,-514,-755
407,-483,-708
564,323,323
-612,734,-767
-448,-754,472

--- scanner 33 ---
718,764,-619
765,-713,-337
530,-652,755
-111,39,39
-894,-897,754
-541,787,536
702,797,-731
602,-823,-351
-521,278,-467
-774,-410,-341
576,825,-655
515,817,730
-542,647,502
511,845,503
560,803,524
-174,-102,136
-489,339,-521
685,-653,-393
-948,-835,742
614,-539,721
-734,-413,-506
-447,735,512
-757,-868,671
662,-737,696
-443,283,-554
-652,-451,-406

--- scanner 34 ---
-268,-488,-296
153,-79,38
-682,711,-374
-719,778,-465
-754,794,-452
-495,-757,490
906,692,876
-266,-388,-374
411,-690,-394
406,-694,-217
454,-761,-296
-290,-463,-419
600,688,-774
644,689,-599
780,-621,788
550,708,-733
-515,843,519
797,513,871
909,-595,795
-540,765,411
39,43,112
-464,-792,569
-648,-778,609
865,656,788
874,-563,720
-660,739,490""".splitlines()

# input = """--- scanner 0 ---
# 404,-588,-901
# 528,-643,409
# -838,591,734
# 390,-675,-793
# -537,-823,-458
# -485,-357,347
# -345,-311,381
# -661,-816,-575
# -876,649,763
# -618,-824,-621
# 553,345,-567
# 474,580,667
# -447,-329,318
# -584,868,-557
# 544,-627,-890
# 564,392,-477
# 455,729,728
# -892,524,684
# -689,845,-530
# 423,-701,434
# 7,-33,-71
# 630,319,-379
# 443,580,662
# -789,900,-551
# 459,-707,401
#
# --- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390
#
# --- scanner 2 ---
# 649,640,665
# 682,-795,504
# -784,533,-524
# -644,584,-595
# -588,-843,648
# -30,6,44
# -674,560,763
# 500,723,-460
# 609,671,-379
# -555,-800,653
# -675,-892,-343
# 697,-426,-610
# 578,704,681
# 493,664,-388
# -671,-858,530
# -667,343,800
# 571,-461,-707
# -138,-166,112
# -889,563,-600
# 646,-828,498
# 640,759,510
# -630,509,768
# -681,-892,-333
# 673,-379,-804
# -742,-814,-386
# 577,-820,562
#
# --- scanner 3 ---
# -589,542,597
# 605,-692,669
# -500,565,-823
# -660,373,557
# -458,-679,-417
# -488,449,543
# -626,468,-788
# 338,-750,-386
# 528,-832,-391
# 562,-778,733
# -938,-730,414
# 543,643,-506
# -524,371,-870
# 407,773,750
# -104,29,83
# 378,-903,-323
# -778,-728,485
# 426,699,580
# -438,-605,-362
# -469,-447,-387
# 509,732,623
# 647,635,-688
# -868,-804,481
# 614,-800,639
# 595,780,-596
#
# --- scanner 4 ---
# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14""".splitlines()

from math import ceil, sqrt


class Scanner:
    def __init__(self):
        self.probes = []
        self.distances = []
        self.distancetable = []
        self.active = True
        self.translation = [0, 0, 0]

    def gen_dis(self):
        self.distances = []
        self.distancetable = []
        for [k, probe] in enumerate(self.probes):
            for [l, probetwo] in enumerate(self.probes):
                if k < l:
                    self.distances.append([abs(probetwo[0] - probe[0]), abs(probetwo[1] - probe[1]), abs(probetwo[2] - probe[2])])
                    self.distances[-1].sort()
                    self.distancetable.append([k, l])
        # print(self.distances)
        # print(self.distancetable)


def rotation_matrix_from_vectors(vec1, vec2):
    oreg = np.zeros((3, 3))
    if vec2[0] == vec1[0]:
        oreg[0][0] = 1
    if vec2[0] == -vec1[0]:
        oreg[0][0] = -1
    if vec2[1] == vec1[0]:
        oreg[0][1] = 1
    if vec2[1] == -vec1[0]:
        oreg[0][1] = -1
    if vec2[2] == vec1[0]:
        oreg[0][2] = 1
    if vec2[2] == -vec1[0]:
        oreg[0][2] = -1

    if vec2[0] == vec1[1]:
        oreg[1][0] = 1
    if vec2[0] == -vec1[1]:
        oreg[1][0] = -1
    if vec2[1] == vec1[1]:
        oreg[1][1] = 1
    if vec2[1] == -vec1[1]:
        oreg[1][1] = -1
    if vec2[2] == vec1[1]:
        oreg[1][2] = 1
    if vec2[2] == -vec1[1]:
        oreg[1][2] = -1

    if vec2[0] == vec1[2]:
        oreg[2][0] = 1
    if vec2[0] == -vec1[2]:
        oreg[2][0] = -1
    if vec2[1] == vec1[2]:
        oreg[2][1] = 1
    if vec2[1] == -vec1[2]:
        oreg[2][1] = -1
    if vec2[2] == vec1[2]:
        oreg[2][2] = 1
    if vec2[2] == -vec1[2]:
        oreg[2][2] = -1

    return oreg


def match(first, second):
    global scanners
    matches = 0
    foundone = False
    matchers = []
    for [i, distance] in enumerate(scanners[first].distances):
        if distance in scanners[second].distances:
            matches += 1
            for [j, oreg] in enumerate(scanners[second].distances):
                if distance == oreg:
                    matchers.append(scanners[second].distancetable[j][0])
                    matchers.append(scanners[second].distancetable[j][1])
                    matchers = list(set(matchers))
                if distance == oreg and not foundone:
                    if distance[0] != distance[1] and distance[1] != distance[2]:
                        foundone = True
                        vec1 = np.array([scanners[first].probes[scanners[first].distancetable[i][0]][0] - scanners[first].probes[
                            scanners[first].distancetable[i][1]][0],
                                scanners[first].probes[scanners[first].distancetable[i][0]][1] - scanners[first].probes[
                                    scanners[first].distancetable[i][1]][1],
                                scanners[first].probes[scanners[first].distancetable[i][0]][2] - scanners[first].probes[
                                    scanners[first].distancetable[i][1]][2]])
                        vec2 = np.array([scanners[second].probes[scanners[second].distancetable[j][0]][0] - scanners[second].probes[
                            scanners[second].distancetable[j][1]][0],
                                scanners[second].probes[scanners[second].distancetable[j][0]][1] - scanners[second].probes[
                                    scanners[second].distancetable[j][1]][1],
                                scanners[second].probes[scanners[second].distancetable[j][0]][2] - scanners[second].probes[
                                    scanners[second].distancetable[j][1]][2]])

    if matches >= 12*11/2:
        print("scanners", first, "and", second, "match with", matches, "distances,", ceil(sqrt(matches*2)), "probes")
        rotation = rotation_matrix_from_vectors(vec2, vec1)
        if np.linalg.det(rotation) != 1:
            rotation = rotation_matrix_from_vectors(-vec2, vec1)
            # print("rotation fixed")
        if np.linalg.det(rotation) != 1:
            print("something's not right")
        # print(vec2, "*", rotation, "=", np.matmul(vec2, rotation), ", Vector1:", vec1)
        # assert all(vec1 == np.matmul(vec2, rotation))
        # find translation
        # translation = np.array([0, 0, 0])
        foundone = False
        for i, distance in enumerate(scanners[second].distances):
            # new_dist = np.matmul(np.asarray(distance), rotation).tolist()
            for [j, oreg] in enumerate(scanners[first].distances):
                if distance == oreg and not foundone:
                    if distance[0] != distance[1] and distance[1] != distance[2]:
                        probe_pos = np.array(scanners[second].probes[scanners[second].distancetable[i][0]])
                        probe_pos = np.matmul(probe_pos, rotation)
                        probe_pos2 = np.array(scanners[first].probes[scanners[first].distancetable[j][0]])
                        scanners[second].translation = probe_pos2 - probe_pos
                        # print(scanners[first].probes)
                        # print(np.matmul(np.asarray(scanners[second].probes[matchers[0]]), rotation).tolist())
                        if (np.matmul(np.asarray(scanners[second].probes[matchers[0]]), rotation) + scanners[second].translation).tolist() in scanners[
                                first].probes:
                            gucci = True
                            for k, probe in enumerate(scanners[second].probes):
                                pos = np.asarray(probe)
                                rot_pos = np.matmul(pos, rotation)
                                final_pos = (rot_pos + scanners[second].translation).tolist()
                                if k in matchers:
                                    # print(final_pos)
                                    # print(scanners[first].probes)
                                    if not final_pos in scanners[first].probes:
                                        gucci = False
                            if gucci:
                                foundone = True
                        else:
                            probe_pos = np.array(scanners[second].probes[scanners[second].distancetable[i][1]])
                            probe_pos = np.matmul(probe_pos, rotation)
                            probe_pos2 = np.array(scanners[first].probes[scanners[first].distancetable[j][0]])
                            scanners[second].translation = probe_pos2 - probe_pos
                        if (np.matmul(np.asarray(scanners[second].probes[matchers[0]]), rotation) + scanners[second].translation).tolist() in scanners[first].probes:
                            gucci = True
                            for k, probe in enumerate(scanners[second].probes):
                                pos = np.asarray(probe)
                                rot_pos = np.matmul(pos, rotation)
                                final_pos = (rot_pos + scanners[second].translation).tolist()
                                if k in matchers:
                                    # print(final_pos)
                                    # print(scanners[first].probes)
                                    if not final_pos in scanners[first].probes:
                                        gucci = False
                            if gucci:
                                foundone = True
                        else:
                            probe_pos = np.array(scanners[second].probes[scanners[second].distancetable[i][0]])
                            probe_pos = np.matmul(probe_pos, rotation)
                            probe_pos2 = np.array(scanners[first].probes[scanners[first].distancetable[j][1]])
                            scanners[second].translation = probe_pos2 - probe_pos
                        if (np.matmul(np.asarray(scanners[second].probes[matchers[0]]), rotation) + scanners[second].translation).tolist() in scanners[first].probes:
                            gucci = True
                            for k, probe in enumerate(scanners[second].probes):
                                pos = np.asarray(probe)
                                rot_pos = np.matmul(pos, rotation)
                                final_pos = (rot_pos + scanners[second].translation).tolist()
                                if k in matchers:
                                    # print(final_pos)
                                    # print(scanners[first].probes)
                                    if not final_pos in scanners[first].probes:
                                        gucci = False
                            if gucci:
                                foundone = True
                        else:
                            probe_pos = np.array(scanners[second].probes[scanners[second].distancetable[i][1]])
                            probe_pos = np.matmul(probe_pos, rotation)
                            probe_pos2 = np.array(scanners[first].probes[scanners[first].distancetable[j][1]])
                            scanners[second].translation = probe_pos2 - probe_pos
                        if (np.matmul(np.asarray(scanners[second].probes[matchers[0]]), rotation) + scanners[second].translation).tolist() in scanners[first].probes:
                            gucci = True
                            for k, probe in enumerate(scanners[second].probes):
                                pos = np.asarray(probe)
                                rot_pos = np.matmul(pos, rotation)
                                final_pos = (rot_pos + scanners[second].translation).tolist()
                                if k in matchers:
                                    # print(final_pos)
                                    # print(scanners[first].probes)
                                    if not final_pos in scanners[first].probes:
                                         gucci = False
                            if gucci:
                                foundone = True
                        else:
                            print("ez sehogy sem jó")
        # print(translation)

        for k, probe in enumerate(scanners[second].probes):
            pos = np.asarray(probe)
            rot_pos = np.matmul(pos, rotation)
            final_pos = (rot_pos + scanners[second].translation).tolist()
            if k in matchers:
                # print(final_pos)
                # print(scanners[first].probes)
                assert final_pos in scanners[first].probes
            if k not in matchers:
                scanners[first].probes.append(final_pos)
        scanners[first].gen_dis()
        # scanners.pop(second)
        scanners[second].active = False
        return True
    else:
        print("scanners 0 and", second, "don't match, only", matches, "distances", ceil(sqrt(matches*2)), "probes")
        return False


scanners = []
for line in input:
    if "scanner" in line:
        scanners.append(Scanner())
    elif "," in line:
        scanners[-1].probes.append([int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2])])
scanners[0].active = False

for scanner in scanners:
    scanner.gen_dis()

while any(scanner.active for scanner in scanners):
    for j in range(len(scanners)):
        if scanners[j].active:
            match(0, j)
print(len(scanners[0].probes))

maxdist = 0
for first in scanners:
    for second in scanners:
        dist = abs(first.translation[0] - second.translation[0]) + abs(first.translation[1] - second.translation[1]) + \
            abs(first.translation[2] - second.translation[2])
        if dist > maxdist:
            maxdist = dist
print(maxdist)


