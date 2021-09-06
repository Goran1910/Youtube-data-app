import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Video } from '../Video';

@Injectable({
  providedIn: 'root'
})
export class VideoService {

  private apiUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getVideosByChannelName(channelName: string): Observable<Video[]>{
    return this.http.get<Video[]>(this.apiUrl + 'videos/' + channelName);
  }

  getVideosByPlaylistName(playlistName: string): Observable<Video[]>{
    return this.http.get<Video[]>(this.apiUrl + 'videos/by/' + playlistName);
  }
}
