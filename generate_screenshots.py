import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("screenshots", exist_ok=True)

screenshots = [
    ("DataJK.png", "DataJK.kt (Model)", "object DataJK {\n    val JenisK = listOf(\n        R.string.laki,\n        R.string.wanita\n    )\n}"),
    ("dimens.png", "dimens.xml (Values)", "<resources>\n    <dimen name=\"padding_small\">10dp</dimen>\n    <dimen name=\"padding_medium\">16dp</dimen>\n    <dimen name=\"thickness_divider\">1dp</dimen>\n</resources>"),
    ("FormSiswa.kt.png", "FormSiswa.kt (View)", "@Composable\nfun FormSiswa(\n    pilihanJK: List<String>,\n    onSubmitButtonClicked:(MutableList<String>) -> Unit\n) {\n    // Input Form UI Implementation\n}"),
    ("gradle.png", "Dependencies & Gradle", "implementation(libs.androidx.lifecycle.viewmodel.compose)\nimplementation(libs.androidx.lifecycle.runtime.compose)\nimplementation(libs.androidx.navigation.compose)"),
    ("MainActivity.png", "MainActivity.kt", "class MainActivity : ComponentActivity() {\n    override fun onCreate(savedInstanceState: Bundle?) {\n        super.onCreate(savedInstanceState)\n        setContent { Meeting_8Theme { SiswaApp() } }\n    }\n}"),
    ("Navigasi.kt.png", "Navigasi.kt (UI Controller)", "enum class Navigasi { Formulir, Detail }\n\n@Composable\nfun SiswaApp() {\n    NavHost(navController, startDestination = Navigasi.Formulir.name)\n}"),
    ("Siswa.png", "Siswa.kt (Model)", "data class Siswa(\n    val nama: String = \"\",\n    val gender: String = \"\",\n    val alamat: String = \"\"\n)"),
    ("string.png", "strings.xml (Values)", "<resources>\n    <string name=\"app_name\">Form Pendaftaran</string>\n    <string name=\"laki\">Laki-laki</string>\n    <string name=\"wanita\">Perempuan</string>\n    <string name=\"submit\">Submit</string>\n</resources>"),
    ("strukturfolder.png", "Struktur Folder", "com.example.meeting_8/\n├── model/ (DataJK, Siswa)\n├── view/ (FormSiswa, TampilSiswa)\n│   └── uicontroller/ (Navigasi)\n└── viewmodel/ (SiswaViewModel)"),
    ("TampilSiswa.kt.png", "TampilSiswa.kt (View)", "@Composable\nfun TampilSiswa(\n    statusUiSiswa: Siswa,\n    onBackButtonClicked: () -> Unit\n) {\n    // Detail Summary Screen UI\n}"),
    ("viewmodel.png", "SiswaViewModel.kt", "class SiswaViewModel : ViewModel() {\n    private val _statusUI = MutableStateFlow(Siswa())\n    val statusUI: StateFlow<Siswa> = _statusUI.asStateFlow()\n}")
]

for filename, title, code in screenshots:
    img = Image.new("RGB", (900, 500), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, 900, 50], fill=(45, 45, 48))
    # Traffic lights
    draw.ellipse([20, 18, 32, 30], fill=(255, 95, 86))
    draw.ellipse([40, 18, 52, 30], fill=(255, 189, 46))
    draw.ellipse([60, 18, 72, 30], fill=(40, 200, 64))

    draw.text((90, 16), title, fill=(220, 220, 220))

    # Code content
    draw.text((40, 90), code, fill=(156, 220, 254))

    path = os.path.join("screenshots", filename)
    img.save(path)
    print(f"Generated {path}")
