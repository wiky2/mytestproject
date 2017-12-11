; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "�ȸ�����������"
!define PRODUCT_VERSION "V0.1"
!define PRODUCT_PUBLISHER "gmbox"
!define PRODUCT_WEB_SITE "http://gmbox.googlecode.com/"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\gmbox.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\orange-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\orange-uninstall.ico"

; Language Selection Dialog Settings
!define MUI_LANGDLL_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_LANGDLL_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_LANGDLL_REGISTRY_VALUENAME "NSIS:Language"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\gmbox.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "SimpChinese"

; Reserve files
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "gmbox_setup.exe"
InstallDir "$PROGRAMFILES\gmbox"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show
BrandingText "�ȸ�����������"

Function .onInit
  !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite try
  File /r "gmbox\*.*"
SectionEnd

Section -AdditionalIcons

  CreateDirectory "$SMPROGRAMS\�ȸ�����������"
  CreateShortCut "$SMPROGRAMS\�ȸ�����������\������վ.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\�ȸ�����������\ж������.lnk" "$INSTDIR\uninst.exe"
  CreateShortCut "$SMPROGRAMS\�ȸ�����������\�ȸ�����������.lnk" "$INSTDIR\gmbox.exe"
  CreateShortCut "$SMPROGRAMS\�ȸ�����������\�ȸ�����������_console.lnk" "$INSTDIR\cli.exe" "" "$INSTDIR\gmbox.exe"
  
  CreateShortCut "$DESKTOP\�ȸ�����������.lnk" "$INSTDIR\gmbox.exe"
  
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"

SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\gmbox.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\gmbox.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) �ѳɹ��ش���ļ�����Ƴ���"
FunctionEnd

Function un.onInit
!insertmacro MUI_UNGETLANGUAGE
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "��ȷʵҪ��ȫ�Ƴ� $(^Name) ���估���е������" IDYES +2
  Abort
FunctionEnd

Section Uninstall

  KillProcDLL::KillProc "gmbox.exe"

  Delete /REBOOTOK "$INSTDIR\*.*"
  RMDir /REBOOTOK /r "$INSTDIR\data"
  RMDir /REBOOTOK /r "$INSTDIR\etc"
  RMDir /REBOOTOK /r "$INSTDIR\lib"
  RMDir /REBOOTOK /r "$INSTDIR\Microsoft.VC90.CRT"
  RMDir /REBOOTOK /r "$INSTDIR\pixbufs"
  RMDir /REBOOTOK "$INSTDIR"

  Delete  /REBOOTOK "$SMPROGRAMS\gmbox\ж������.lnk"
  Delete  /REBOOTOK "$SMPROGRAMS\gmbox\������վ.lnk"
  Delete  /REBOOTOK "$SMPROGRAMS\gmbox\�ȸ�����������_console.lnk"
  Delete  /REBOOTOK "$SMPROGRAMS\�ȸ�����������\�ȸ�����������.lnk"
  RMDir   /REBOOTOK "$SMPROGRAMS\�ȸ�����������"
  
  Delete  /REBOOTOK "$DESKTOP\�ȸ�����������.lnk"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd