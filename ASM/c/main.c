#include "chests.h"
#include "debug.h"
#include "dpad.h"
#include "dungeon_info.h"
#include "extern_ctxt.h"
#include "file_select.h"
#include "ganon.h"
#include "get_items.h"
#include "gfx.h"
#include "hud_colors.h"
#include "inputviewer.h"
#include "message.h"
#include "misc_colors.h"
#include "model_text.h"
#include "models.h"
#include "music.h"
#include "sage_gifts.h"
#include "scene.h"
#include "text.h"
#include "textures.h"
#include "triforce.h"
#include "twinrova.h"
#include "uninvertYaxis.h"
#include "util.h"
#include "weather.h"
#include "z64.h"

void Gameplay_InitSkybox(z64_game_t* globalCtx, int16_t skyboxId);

void c_init() {
	heap_init();
	gfx_init();
	text_init();
	item_overrides_init();
	override_flags_init();
	models_init();
	init_textures();
}

void before_game_state_update() {
	handle_pending_items();
	handle_dpad();
	update_misc_colors();
	update_hud_colors();
	process_extern_ctxt();
	manage_music_changes();
	manage_uninvert_yaxis();
	display_misc_messages();
}

void after_game_state_update() {
	// Checks if the prerender screen is being drawn before drawing new HUD
	// things. Else this will cause graphical and/or lag issues on some emulators
	// when pausing.
	if (R_PAUSE_BG_PRERENDER_STATE != PAUSE_BG_PRERENDER_PROCESS) {
		draw_dungeon_info(&(z64_ctxt.gfx->overlay));
		draw_triforce_count(&(z64_ctxt.gfx->overlay));
		draw_boss_key(&z64_game, &(z64_ctxt.gfx->overlay));
		draw_silver_rupee_count(&z64_game, &(z64_ctxt.gfx->overlay));
		draw_illegal_model_text(&(z64_ctxt.gfx->overlay));
		draw_input_viewer(&(z64_ctxt.gfx->overlay));
		display_song_name(&(z64_ctxt.gfx->overlay));
		debug_utilities(&(z64_ctxt.gfx->overlay));
	}
	give_sage_gifts();
}

void before_skybox_init(z64_game_t* game, int16_t skyboxId) {
	override_weather_state();
	Gameplay_InitSkybox(game, skyboxId);
}

void after_scene_init() {
	check_ganon_entry();
	clear_twinrova_vars();
	models_reset();
	extern_scene_init();
	check_model_skeletons();
	reset_collectible_mutex();
	get_current_scene_setup_number();
}
