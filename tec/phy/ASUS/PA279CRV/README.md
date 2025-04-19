# ✅ PA279CRV Golden State (Confirmed Working Setup)

## 🖥️ Monitor
- Model: ASUS PA279CRV
- Connection: HDMI 2.0 (direct from NUC, no KVM)
- Cable: Certified HDMI 2.0 or 2.1 (short + known-good)

## 🧠 GPU / System
- System: Intel NUC 11ATKC4
- GPU: Intel UHD Graphics (Jasper Lake)
- Drivers: Latest from Intel.com (not Windows Update)
- Display Output: Native HDMI port only (no DP→HDMI adapter)

## 🧰 CRU Configuration
- **Entry in CRU**: `AUS27E1 - PA279CRV (active)`
- **Detailed Resolutions**:
  - `3840 × 2160 @ 60.000 Hz (594.00 MHz)` — top of list ✅

- **Standard Resolutions**:
  - 1920×1080 @ 60 Hz
  - 1280×720 @ 60 Hz
  - 1680×1050 @ 60 Hz
  - 1440×900 @ 60 Hz
  - 1280×960 @ 60 Hz
  - 1280×1024 @ 60 Hz
  - 1280×800 @ 60 Hz
  - 1600×1200 @ 60 Hz

- **Established Resolutions**:
  - Legacy 4:3 (640×480, 800×600, 1024×768) — safe fallback

- **Extension Block**:
  - Type: CTA-861
  - Contains: 1 detailed resolution, 10 data blocks (HDMI 2.1-capable EDID)

## 🧪 Windows Settings
- Resolution: `3840 × 2160`
- Refresh Rate: `60 Hz` (actual: `59.94 Hz`)
- Scaling: 100% (for full crispness)
- Active Signal Mode: `3840 × 2160 @ 59.94 Hz`
- Color Format: RGB (Full)
- Bit Depth: 8-bit
- Color Space: SDR (unless HDR is enabled)

## 🧼 EDID/CRU Tips
- No unnecessary CRU overrides
- No extension block deletions
- No forced custom timings
- Use CRU only for inspection or backup in this state

## 💾 Recommended Backup
- Use CRU’s **Export** button to save `.bin` config now
- Name it: `PA279CRV_GoldenState_Backup.bin`

---

# ✅ PA279CRV Golden State – KVM-Compatible Edition

## 🖥️ Monitor
- Model: ASUS PA279CRV
- Input used: **HDMI2**
- Status: 4K@60 confirmed, crisp display, EDID clean
- Cable: High-quality HDMI 2.0/2.1

## 🧠 GPU / System
- System: Intel NUC 11ATKC4
- GPU: Intel UHD Graphics (Jasper Lake)
- Output: Native HDMI port only
- Driver: Latest from Intel.com
- CRU: Active (Custom 29.97 Hz fallback installed)

## 🖧 KVM Switch
- Model: TESmart HKS402
- EDID mode: Fixed/emulated
- Reset performed: ✅ (factory reset prior to test)
- Output2 (second monitor) **disconnected** during test
- Only PA279CRV connected on **Output1**
- Boot sequence:
  1. Power off NUC
  2. Factory reset KVM
  3. Disconnect all but PA279CRV
  4. Power on monitor (HDMI2 selected)
  5. Power on KVM
  6. Power on NUC

## 🔑 Key Finding
> KVM setup **preserved the original EDID path**.  
> CRU and Windows detect **only one monitor instance** (same device ID).  
> Custom refresh modes (e.g., 29.97 Hz) remain valid and selectable.  
> No fallback to “Generic Monitor” or truncated resolution list.

## 🧰 CRU Configuration
- **Monitor entry**: `AUS27E1 - PA279CRV (active)`
- **Detailed resolutions**:
  - 3840×2160 @ 60.000 Hz
  - 3840×2160 @ 29.970 Hz (manual, HDMI-safe fallback)
- **Standard resolutions**: Common fallbacks (1080p, 1600x1200, etc.)
- **Extension block**: CTA-861 with 10 HDMI 2.1 data blocks

## 🖼️ Windows Settings
- Resolution: 3840×2160
- Refresh Rate: 60 Hz (default) / 29.97 Hz (optional fallback)
- Color Format: RGB (Full)
- Bit Depth: 8-bit
- HDR: Not certified (but EDID HDR flags may be present)

## 💾 Backup Recommended
- Export current CRU state (`.bin`) as:
  - `PA279CRV_KVM_Baseline.bin`
