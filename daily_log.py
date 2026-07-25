import os
import datetime
import json

LOGS_DIR = "logs"
STATS_FILE = "stats.json"

def ensure_dirs():
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs("projects", exist_ok=True)
    os.makedirs("resources", exist_ok=True)

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "total_days": 0,
        "total_projects": 0,
        "total_lines_of_code": 0,
        "algorithm_solved": 0,
        "current_phase": 1,
        "streak_days": 0,
        "last_study_date": None,
        "start_date": "2026-07-25"
    }

def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

def get_today_file():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOGS_DIR, f"{today}.md")

def create_log_template():
    today = datetime.datetime.now()
    date_str = today.strftime("%A, %d %B %Y")
    
    template = f"""# Log Belajar - {date_str}

## Tujuan Hari Ini
- [ ] 
- [ ] 

## Materi yang Dipelajari
### Topik:
- 

### Sumber:
- 

### Catatan Penting:
- 

## Coding & Praktik
### Project/File:
- 

### Baris Kode:
- 

### Error yang Dihadapi & Solusi:
- Error: 
- Solusi: 

## Soal Algoritma / Latihan
| Platform | Soal | Status | Catatan |
|----------|------|--------|---------|
| | | OK/NO | |

## Waktu Belajar
- Mulai: 
- Selesai: 
- Total:  jam  menit

## Refleksi Hari Ini
Berhasil:
- 

Perlu Ditingkatkan:
- 

Rencana Besok:
- 

---
Dilengkapi oleh Bas
"""
    return template

def main():
    ensure_dirs()
    stats = load_stats()
    
    today_file = get_today_file()
    
    if os.path.exists(today_file):
        print("Log hari ini sudah ada!")
        print(f"   File: {today_file}")
    else:
        with open(today_file, "w", encoding="utf-8") as f:
            f.write(create_log_template())
        
        stats["total_days"] += 1
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        if stats["last_study_date"]:
            last = datetime.datetime.strptime(stats["last_study_date"], "%Y-%m-%d")
            curr = datetime.datetime.strptime(today, "%Y-%m-%d")
            diff = (curr - last).days
            if diff == 1:
                stats["streak_days"] += 1
            elif diff > 1:
                stats["streak_days"] = 1
        else:
            stats["streak_days"] = 1
            
        stats["last_study_date"] = today
        save_stats(stats)
        
        print("Log hari ini berhasil dibuat!")
        print(f"   File: {today_file}")
        print(f"   Streak: {stats['streak_days']} hari berturut-turut")
    
    print("\nStatistik Saat Ini:")
    print(f"   Total Hari Belajar: {stats['total_days']}")
    print(f"   Total Project: {stats['total_projects']}")
    print(f"   Soal Algoritma: {stats['algorithm_solved']}")
    print(f"   Fase Saat Ini: {stats['current_phase']}")

if __name__ == "__main__":
    main()
