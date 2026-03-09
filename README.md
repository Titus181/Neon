# 🎰 Neon Spin Simulator & Math Model

Welcome to the **Neon Spin** project! This repository contains the frontend visual simulator, the core math model design, and the Monte Carlo simulation results for a fast-paced lucky wheel game show.

### 🔗 Quick Links
* **[🎮 Play the Online Simulator](https://titus181.github.io/Neon/)**
* **[📊 Math Model Google Spreadsheet](https://docs.google.com/spreadsheets/d/1joYiLXAZEIoLnz15BvJ5dMqdYvYzuejGCUUPQYa6cIo/edit?gid=0#gid=0)**

---

## 📖 Game Rules

### 1. Game Overview
Neon Spin is a simple, fast-paced lucky wheel game show. The wheel consists of **54 segments**, featuring 4 different numbers and a special "Mystery Box" segment.

### 2. How to Play
Players can place their bets on 5 available options: `Number 1`, `Number 2`, `Number 5`, `Number 10`, or the `Mystery Box`. Once betting time is over, the presenter will spin the lucky wheel.

### 3. Lucky Multipliers
Before the wheel is spun, extra random multipliers are drawn and distributed to **1 or 2 regular segments** each game round.
If the wheel stops on a segment with a multiplier, this enhanced multiplier will **replace** the standard payout value for the selected number.
* **[Upgrade Guarantee]**: The applied lucky multiplier will ALWAYS be strictly higher than the base payout of that segment! For instance, if a multiplier lands on Number 10, it is guaranteed to be 15x or higher, ensuring a much bigger win!
* **Note**: Random multipliers do not apply to the Mystery Box segment.

### 4. Mystery Box Bonus
Triggered when the wheel stops on the Mystery Box segment. Every player with a valid bet on the Mystery Box in the current game round is eligible to take part.
**3 chests** will appear on the screen. Players have 5 seconds to pick 1 chest of their choice. If a player misses the selection time, the system will select one box randomly on their behalf. Each chest contains a hidden multiplier. Players will be rewarded according to the multiplier inside their chosen box.

### 5. Standard Payouts
* **Number 1**: Pays 1:1
* **Number 2**: Pays 2:1
* **Number 5**: Pays 5:1
* **Number 10**: Pays 10:1
* **Mystery Box**: Pays according to the revealed multiplier.

---

## 🧮 Math Model Overview

The math model is designed to provide a stable Return to Player (RTP) while creating high-multiplier excitement through the Lucky Multipliers and the Mystery Box. The overall theoretical RTP is balanced between **96.44% and 96.51%**.

| Bet Option | Total Return (Inc. Bet) | Segments | Hit Rate | Theoretical RTP |
| :--- | :--- | :--- | :--- | :--- |
| **1x** | 2 | 21 | 38.89% | 96.48% |
| **2x** | 3 | 14 | 25.93% | 96.50% |
| **5x** | 6 | 7 | 12.96% | 96.50% |
| **10x** | 11 | 4 | 7.41% | 96.51% |
| **Mystery Box** | Variable (Box Reveal) | 8 | 14.81% | 96.44% |

*(For detailed Bonus weighting pools and Mystery Box probabilities, please refer to the Math Model Spreadsheet linked above.)*

---

## 🚀 1 Billion Rounds Simulation Results

To verify the accuracy of our mathematical model and code logic, a Monte Carlo simulation of **1,000,000,000 (1 Billion) rounds** was executed. 

The results show that the simulated RTP converges extremely closely with the theoretical RTP, with variance strictly within `0.04%`.

```text
🏁 All simulations completed! Total time: 3422.40 seconds

--------------------------------------------------
Bet Option       | Sim RTP      | Theo RTP     | Diff
--------------------------------------------------
Bet 1x           |  96.4909%    |  96.4800%    | +0.0109%
Bet 2x           |  96.5007%    |  96.5000%    | +0.0007%
Bet 5x           |  96.4866%    |  96.5000%    | -0.0134%
Bet 10x          |  96.4709%    |  96.5100%    | -0.0391%
Mystery Box      |  96.4516%    |  96.4400%    | +0.0116%
--------------------------------------------------
```

---

# 🎰 Neon Spin 模擬器與數值模型

《Neon Spin》是一款簡單、快節奏的輪盤遊戲。本專案包含遊戲的純前端實境模擬器、核心數值模型（Math Model）設計，以及大樣本蒙地卡羅模擬（Monte Carlo Simulation）的驗證結果。

### 🔗 相關連結
* **[🎮 遊玩線上模擬器](https://titus181.github.io/Neon/)**
* **[📊 數值模型 Google 試算表](https://docs.google.com/spreadsheets/d/1joYiLXAZEIoLnz15BvJ5dMqdYvYzuejGCUUPQYa6cIo/edit?gid=0#gid=0)**

---

## 📖 遊戲說明 (Game Rules)

### 1. 遊戲簡介
輪盤總共分為 **54 個區塊**，包含 4 種常規數字區塊以及專屬的「神祕盒 (Mystery Box)」區塊。
玩家可以自由將籌碼押注在 5 個選項上：`1x`、`2x`、`5x`、`10x`，或是 `Mystery Box`。

### 2. 隨機幸運倍率 (Lucky Multipliers)
在輪盤轉動前，系統會為每局遊戲隨機抽出額外的「幸運倍率」，並分配到 **1 或 2 個常規區塊**上。
若輪盤最終停在帶有幸運倍率的區塊上，該倍率將會**直接取代**原先的基礎賠付！
* **倍率升級保證**：附加的幸運倍率絕對會「高於」該選項原本的基礎賠率。例如押中 10 倍區塊，幸運倍率保證從 15 倍起跳。
* **注意**：幸運倍率僅會附加在常規數字上，不會出現在神祕盒區塊。

### 3. 神祕盒獎勵 (Mystery Box Bonus)
當輪盤停在「神祕盒」區塊時，本局有在該選項下注的玩家即可進入神祕盒環節。
畫面上將會出現 3 個寶箱，每個寶箱內皆藏有不同的高低倍率。玩家必須在 5 秒內點擊選擇其中 1 個寶箱，打開後將根據抽中的專屬倍率獲得對應獎金。

---

## 🧮 數值模型說明 (Math Model)

本遊戲的數值架構設計旨在提供穩定的 RTP（玩家回報率），同時透過 Lucky Multipliers 與 Mystery Box 創造高倍率的爆發期待感。整體理論 RTP 均控制在 **96.44% ~ 96.51%** 之間。

### 輪盤分佈與基礎賠付
| 押注選項 | 賠付 (含本金) | 區塊數量 (Segments) | 轉中機率 (Hit Rate) | 理論 RTP |
| :--- | :--- | :--- | :--- | :--- |
| **1x** | 2 | 21 | 38.89% | 96.48% |
| **2x** | 3 | 14 | 25.93% | 96.50% |
| **5x** | 6 | 7 | 12.96% | 96.50% |
| **10x** | 11 | 4 | 7.41% | 96.51% |
| **Mystery Box** | 浮動 (依寶箱) | 8 | 14.81% | 96.44% |

*(詳細的 Bonus 權重池與 Mystery Box 抽樣機率，請參閱上方提供的數值模型試算表。)*

---

## 🚀 10 億次模擬結果 (Simulation Results)

為了驗證數值模型的準確性與程式邏輯的正確性，我們針對遊戲邏輯進行了 **10 億次 (1 Billion Rounds)** 的蒙地卡羅模擬。

結果顯示，實測 RTP 與理論 RTP 的誤差皆收斂在 `0.04%` 以內，證明機率模型運作極為精準且穩定。

```text
🏁 全部模擬完成！總耗時: 3422.40 秒

--------------------------------------------------
下注選項         | 模擬 RTP     | 理論 RTP     | 誤差
--------------------------------------------------
Bet 1x       |  96.4909% |  96.4800% | +0.0109%
Bet 2x       |  96.5007% |  96.5000% | +0.0007%
Bet 5x       |  96.4866% |  96.5000% | -0.0134%
Bet 10x      |  96.4709% |  96.5100% | -0.0391%
Mystery Box  |  96.4516% |  96.4400% | +0.0116%
--------------------------------------------------
```