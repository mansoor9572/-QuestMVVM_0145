# QuestMVVM_0145

An Android application built with Jetpack Compose implementing MVVM architecture, StateFlow, and Navigation Compose for student registration and details display.

## Project Structure & Implementation Screenshots

### 1. Struktur Folder (Project Structure)
- Package layout containing `model`, `view`, `viewmodel`, and `uicontroller`.

### 2. Model Siswa (`Siswa.kt`)
- Data class storing student data (`nama`, `gender`, `alamat`).

### 3. DataJK (`DataJK.kt`)
- Object mapping gender string resources (`laki`, `wanita`).

### 4. String Resources (`strings.xml`)
- Application strings for form labels, headers, and buttons.

### 5. Dimension Resources (`dimens.xml`)
- Padding and divider thickness dimensions.

### 6. Dependencies (`build.gradle.kts` / `libs.versions.toml`)
- Jetpack Compose BOM, ViewModel Compose, Lifecycle Compose, and Navigation Compose.

### 7. SiswaViewModel (`SiswaViewModel.kt`)
- StateFlow managing student state and update logic.

### 8. FormSiswa (`FormSiswa.kt`)
- Input form screen with OutlinedTextField, RadioButton selection, and Submit button.

### 9. TampilSiswa (`TampilSiswa.kt`)
- Detail screen displaying submitted student information and Back button.

### 10. Navigasi (`Navigasi.kt`)
- Navigation graph controlling flow between Form and Detail screens.

### 11. MainActivity (`MainActivity.kt`)
- Host activity launching SiswaApp with Edge-to-Edge support.
