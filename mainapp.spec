# -*- mode: python ; coding: utf-8 -*-

added_files = [
    ('.env', '.'),
    ('LICENSE', '.'),
    ('interfaz/y', '.'),
   
]

a = Analysis(
    ['interfaz/mainapp.py'],
    pathex=[],
    binaries=[],
    datas=added_files,,
          
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='mobility',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mobility',
)
