package com.example.meeting_8

import com.example.meeting_8.model.Sisa
import com.example.meeting_8.model.Siswa
import org.junit.Test
import org.junit.Assert.*

/**
 * Unit tests for Siswa model and general assertions.
 */
class ExampleUnitTest {
    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)
    }

    @Test
    fun siswa_model_default_values() {
        val siswa = Siswa()
        assertEquals("", siswa.nama)
        assertEquals("", siswa.gender)
        assertEquals("", siswa.alamat)
    }
}
