import random
import time
import numpy as np

def run_neon_spin_simulation(num_rounds=1_000_000, model_version="v1"):
    print(f"🚀 開始執行 Neon Spin 蒙地卡羅模擬 (版本: {model_version.upper()}, 共 {num_rounds:,} 局)...")
    
    # 根據選擇的模型版本載入設定
    if model_version == "v1":
        # === V1 數值模型 (原始版本) ===
        # 1. 建立輪盤 (0: 1x, 1: 2x, 2: 5x, 3: 10x, 4: 神秘盒) 總計 54 格
        wheel = [0]*21 + [1]*14 + [2]*7 + [3]*4 + [4]*8
        
        # 2. 定義四軌 Bonus 權重池 (倍率陣列, 機率陣列)
        pools = {
            0: (np.array([5, 10, 15, 20, 25, 50]), np.array([0.20, 0.21, 0.23, 0.06, 0.28, 0.02])),
            1: (np.array([5, 10, 15, 20, 25, 50, 100]), np.array([0.05, 0.07, 0.22, 0.17, 0.36, 0.11, 0.02])),
            2: (np.array([10, 15, 25, 50, 100, 250]), np.array([0.08, 0.45, 0.23, 0.03, 0.12, 0.09])),
            3: (np.array([15, 25, 50, 100, 250, 500]), np.array([0.08, 0.58, 0.06, 0.21, 0.01, 0.06]))
        }
        
        # 3. Bonus 數量機率
        num_bonuses_choices = [1, 2]
        num_bonuses_probs = [0.50, 0.50]
        
        # 4. 神祕盒抽獎邏輯 (賠付含本金 Total Return, 機率陣列)
        box_a = (np.array([3]), np.array([1.0]))
        box_b = (np.array([4, 6]), np.array([0.76, 0.24]))
        box_c = (np.array([11, 16, 26, 51]), np.array([0.88, 0.10, 0.01, 0.01]))
        
        # 理論 RTP
        theoretical = [96.48, 96.50, 96.50, 96.51, 96.44]

    elif model_version == "v2":
        # === V2 數值模型 (4 Mystery Boxes 版本) ===
        # 1. 建立輪盤 (0: 1x, 1: 2x, 2: 5x, 3: 10x, 4: 神秘盒) 總計 54 格
        wheel = [0]*24 + [1]*15 + [2]*7 + [3]*4 + [4]*4
        
        # 2. 定義四軌 Bonus 權重池 (倍率陣列, 機率陣列 - 依照最新 4 位小數版本更新)
        pools = {
            0: (np.array([5, 10, 15, 20, 25, 50]), np.array([0.70, 0.12, 0.07, 0.06, 0.03, 0.02])),
            1: (np.array([5, 10, 15, 20, 25, 50, 100]), np.array([0.05, 0.07, 0.22, 0.17, 0.36, 0.11, 0.02])),
            2: (np.array([10, 15, 25, 50, 100, 250]), np.array([0.10, 0.30, 0.23, 0.19, 0.11, 0.07])),
            3: (np.array([15, 25, 50, 100, 250, 500]), np.array([0.09, 0.40, 0.18, 0.21, 0.08, 0.04]))
        }
        
        # 3. Bonus 數量機率 (1: 85%, 2: 15%)
        num_bonuses_choices = [1, 2]
        num_bonuses_probs = [0.85, 0.15]
        
        # 4. 神祕盒抽獎邏輯 (賠付含本金 Total Return, 機率陣列)
        box_a = (np.array([3, 4, 6, 11]), np.array([0.70, 0.20, 0.07, 0.03]))
        box_b = (np.array([4, 6, 8, 11, 16, 21, 26, 31]), np.array([0.44, 0.17, 0.15, 0.10, 0.06, 0.04, 0.03, 0.01]))
        
        # Box C 依照最新版本的精確小數位數設定 (總和為 100.0000%)
        box_c_probs = np.array([0.50, 0.24, 0.106, 0.0544, 0.047, 0.021, 0.015, 0.0155, 0.001, 0.0001])
        # 為避免浮點數精度 (如 0.9999999999999999) 導致 numpy 報錯，進行標準化
        box_c_probs = box_c_probs / box_c_probs.sum()
        box_c = (np.array([11, 16, 26, 51, 101, 126, 151, 176, 201, 251]), box_c_probs)

        # 理論 RTP
        theoretical = [96.76, 97.48, 90.97, 93.64, 96.55]
        
    else:
        raise ValueError("不支援的模型版本，請選擇 'v1' 或 'v2'")

    # 找出所有常規區塊的索引
    regular_indices = [i for i, val in enumerate(wheel) if val != 4]
    
    # 統計變數
    bets = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    wins = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    
    # 基礎賠付 (含本金)
    base_returns = {0: 2, 1: 3, 2: 6, 3: 11}
    
    start_time = time.time()
    last_checkpoint = start_time

    for round_num in range(1, num_rounds + 1):
        # 決定本局 Bonus 數量與賦予的實體區塊位置
        num_bonuses = np.random.choice(num_bonuses_choices, p=num_bonuses_probs)
        bonus_targets = random.sample(regular_indices, num_bonuses)
        
        # 轉動輪盤，決定最終停放的實體區塊
        result_idx = random.randrange(54)
        result_type = wheel[result_idx]
        
        # 模擬玩家在 5 個選項各下注 1 單位
        for bet_type in range(5):
            bets[bet_type] += 1
            
            # 只有當「轉中結果」等於「玩家下注選項」時才派彩
            if bet_type == result_type:
                if bet_type != 4: 
                    # === 常規區塊邏輯 ===
                    if result_idx in bonus_targets:
                        # 該區塊剛好被 Bonus 覆蓋，從對應權重池抽倍率
                        mult = np.random.choice(pools[bet_type][0], p=pools[bet_type][1])
                        # 賠付含本金 = 純倍率 + 1
                        wins[bet_type] += (mult + 1) 
                    else:
                        # 獲得基礎賠付
                        wins[bet_type] += base_returns[bet_type]
                else: 
                    # === 神秘盒邏輯 (分區抽樣後三選一) ===
                    val_a = np.random.choice(box_a[0], p=box_a[1])
                    val_b = np.random.choice(box_b[0], p=box_b[1])
                    val_c = np.random.choice(box_c[0], p=box_c[1])
                    
                    # 玩家隨機點擊畫面上的其中一個寶箱
                    chosen_val = random.choice([val_a, val_b, val_c])
                    wins[bet_type] += chosen_val
                    
        if round_num % 10_000_000 == 0:
            now = time.time()
            segment_time = now - last_checkpoint
            elapsed = now - start_time
            print(f"✅ 已完成 {round_num:>14,} 局 | 本段耗時: {segment_time:.2f}s | 累計耗時: {elapsed:.2f}s")
            last_checkpoint = now

    total_time = time.time() - start_time
    print(f"\n🏁 全部模擬完成！總耗時: {total_time:.2f} 秒\n")

    # 印出結果對比
    labels = ["Bet 1x", "Bet 2x", "Bet 5x", "Bet 10x", "Mystery Box"]
    
    print("-" * 50)
    print(f"{'下注選項':<12} | {'模擬 RTP':<10} | {'理論 RTP':<10} | {'誤差'}")
    print("-" * 50)
    for i in range(5):
        rtp = (wins[i] / bets[i]) * 100
        diff = rtp - theoretical[i]
        print(f"{labels[i]:<12} | {rtp:>8.4f}% | {theoretical[i]:>8.4f}% | {diff:>+7.4f}%")
    print("-" * 50)

# 執行 1 億次模擬 
run_neon_spin_simulation(100_000_000_0, model_version="v2")