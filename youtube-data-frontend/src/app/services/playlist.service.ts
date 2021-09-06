import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Playlist } from '../Playlist';

@Injectable({
  providedIn: 'root'
})

export class PlaylistService {

  private apiUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getPlaylists(channelName: string): Observable<Playlist[]>{
    return this.http.get<Playlist[]>(`${this.apiUrl}playlists/${channelName}`);
  }

  getPlaylistsTitles(channelName: string): Observable<String[]>{
    return this.http.get<String[]>(`${this.apiUrl}playlists/titles/${channelName}`);
  }
}
